from __future__ import annotations

import os
from typing import (
    List,
    Optional,
    Any,
    Callable,
    Dict,
    TypeVar,
    Generic,
    Union,
    Generator,
)

from dataclasses import dataclass

from functional_workflow.config import read_config
from functional_workflow.logger import log
from functional_workflow.reader import read_input
from functional_workflow.writer import write_output


@dataclass
class WorkflowDataTray:
    config: Dict
    data: List[Any]


@dataclass
class WorkflowResult:
    payload: Optional[Any] = None
    success: bool = True
    message: Optional[str] = None

    @staticmethod
    def unit(value):
        return WorkflowResult(payload=value)

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


StepFunction = Callable[[Any], Optional[WorkflowResult]]


def read_config_step() -> WorkflowResult:
    return WorkflowResult(payload=read_config("cfg/config.ini"))


def read_source_step(config: Dict) -> Optional[WorkflowResult]:
    file_name = config["input_file"]
    return WorkflowResult(payload=read_input(file_name))


def log_current_step(value: Any) -> Optional[WorkflowResult]:
    log(f"--> Processing: {str(value)}")
    return WorkflowResult()


def compose_output_file_name(entry: str, config: Dict):
    return os.path.join(
        config["output_directory"],
        f'{config["output_file_prefix"]}_{entry[:10].strip()}.txt',
    )


def write_output_step(config: Dict, data: Any) -> Optional[WorkflowResult]:
    for entry_data in data:
        output_file_name = compose_output_file_name(entry_data, config)
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
