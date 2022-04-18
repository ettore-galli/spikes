from __future__ import annotations

import os
from typing import Optional, Any, Callable, Dict, TypeVar, Generic, Union, Generator

from attr import dataclass

from functional_workflow.config import read_config
from functional_workflow.logger import log
from functional_workflow.reader import read_input
from functional_workflow.writer import write_output

P = TypeVar("P")
C = TypeVar("C")


class WorkflowPayload:
    data: Optional[Any] = None
    config: Optional[Dict] = None

    def __init__(self, data=None, config=None):
        self.data = data
        self.config = config

    def merge(self, data=None, config=None):
        return WorkflowPayload(
            data=data if data else self.data, config=config if config else self.config
        )

    def with_data(self, data):
        return WorkflowPayload(data=data, config=self.config)


class WorkflowResult(Generic[P, C]):
    def __init__(
        self,
        payload: Optional[WorkflowPayload] = None,
        success: bool = True,
        message: Optional[str] = None,
    ):
        self.payload = payload
        self.success = success
        self.message = message

    @staticmethod
    def unit(value):
        return WorkflowResult(payload=value)

    @staticmethod
    def merge(previous: WorkflowResult, new: WorkflowResult):
        return WorkflowResult(
            payload=new.payload or previous.payload,
            success=new.success and previous.success,
            message=new.message or "",
        )

    def bind(
        self,
        f: StepFunction,
    ):
        if not self.success:
            return self
        try:
            result = f(self.payload)
            return self.merge(self, result) if result else self

        except Exception as exception:
            return WorkflowResult(
                payload=self.payload, success=False, message=str(exception)
            )

    def __repr__(self) -> str:
        return (
            "Workflow Result:"
            f"\n - Payload : {self.payload or '<no payload>'}"
            f"\n - Success : {self.success} "
            f"\n - Message : {self.message or 'OK'}"
        )

    def __rshift__(self, other):
        return self.bind(other)

    def __and__(self, other):
        return self.bind(other)

    def __or__(self, other):
        return self.bind(other)

    def __gt__(self, other):
        return self.bind(other)


StepFunction = Callable[[WorkflowPayload], Optional[WorkflowResult]]


def read_config_step(_: Any) -> WorkflowResult:
    return WorkflowResult(payload=WorkflowPayload(config=read_config("cfg/config.ini")))


def read_source_step(value: WorkflowPayload) -> Optional[WorkflowResult]:
    file_name = value.config["input_file"]
    return WorkflowResult(payload=value.merge(data=read_input(file_name)))


def log_current_step(value: WorkflowPayload) -> Optional[WorkflowResult]:
    log(f"--> Processing: {str(value.data)}")
    return None


def compose_output_file_name(entry: str, config: Dict):
    return os.path.join(
        config["output_directory"],
        f'{config["output_file_prefix"]}_{entry[:10].strip()}.txt',
    )


def write_output_step(value: WorkflowPayload) -> Optional[WorkflowResult]:
    for entry_data in value.data:
        output_file_name = compose_output_file_name(entry_data, value.config)
        write_output(entry_data, output_file_name)

    return None


if __name__ == "__main__":

    main = (
        WorkflowResult.unit(None)
        >> read_config_step
        >> read_source_step
        >> write_output_step
    )

    print(main)
