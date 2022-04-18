from __future__ import annotations

import os
from typing import Optional, Any, Callable, Dict, TypeVar, Generic, Union, Generator

from functional_workflow.config import read_config
from functional_workflow.logger import log
from functional_workflow.reader import read_input
from functional_workflow.writer import write_output

P = TypeVar("P")
C = TypeVar("C")

WorkflowData = str


class lazyWorkflowResult(Generic[P, C]):
    def __init__(
        self,
        payload: Optional[Union[P, Generator[P, None, None]]] = None,
        config: Optional[C] = None,
        success: bool = True,
        message: Optional[str] = None,
    ):
        self.payload = payload
        self.config = config
        self.success = success
        self.message = message

    @staticmethod
    def unit(value):
        return lazyWorkflowResult(payload=value)

    @staticmethod
    def merge(previous: lazyWorkflowResult, new: lazyWorkflowResult):
        return lazyWorkflowResult(
            payload=new.payload or previous.payload,
            config=new.config or previous.config,
            success=new.success and previous.success,
            message=new.message or "",
        )

    def bind(
        self,
        f: Union[
            Callable[[lazyWorkflowResult], lazyWorkflowResult],
            Callable[[lazyWorkflowResult], Generator[lazyWorkflowResult, None, None]],
        ],
    ):
        if not self.success:
            return self
        try:
            result = f(self)
            return self.merge(self, result)

        except Exception as exception:
            return lazyWorkflowResult(
                payload=self.payload, success=False, message=str(exception)
            )

    def __repr__(self) -> str:
        return (
            "Workflow Result:"
            f"\n - Config  : {self.config or '<no config>'}"
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


def read_config_step(_: Any) -> lazyWorkflowResult:
    return lazyWorkflowResult(config=read_config("cfg/config.ini"))


def read_source_step(value: lazyWorkflowResult) -> lazyWorkflowResult:
    file_name = value.config["input_file"]
    return lazyWorkflowResult(payload=read_input(file_name))


def log_current_step(value: lazyWorkflowResult) -> lazyWorkflowResult:
    log(f"--> Processing: {str(value.payload)}")
    return value


def compose_output_file_name(entry: str, config: Dict):
    return os.path.join(
        config["output_directory"],
        f'{config["output_file_prefix"]}_{entry[:10].strip()}.txt',
    )


def write_output_step(value: lazyWorkflowResult) -> lazyWorkflowResult:
    for entry_data in value.payload:
        output_file_name = compose_output_file_name(entry_data, value.config)
        write_output(entry_data, output_file_name)

    return lazyWorkflowResult()


if __name__ == "__main__":

    main = (
        lazyWorkflowResult[WorkflowData, Dict]().unit(None)
        >> read_config_step
        >> read_source_step
        >> write_output_step
    )

    print(main)
