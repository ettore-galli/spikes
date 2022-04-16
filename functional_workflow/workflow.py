from __future__ import annotations

from dataclasses import dataclass
from typing import Optional, Any, Callable, List, Dict

from functional_workflow.config import read_config
from functional_workflow.reader import read_input


@dataclass
class WorkflowData:
    config: Optional[Dict] = None
    entries: Optional[List[str]] = None

    def __repr__(self) -> str:
        return f"{self.config}\n" \
               f"{self.entries}\n"

    @staticmethod
    def merge(previous: Optional[WorkflowData], new: Optional[WorkflowData]) -> WorkflowData:
        return WorkflowData(
            config=previous.config if previous and previous.config else new.config,
            entries=previous.entries if previous and previous.entries else new.entries
        )


class WorkflowBase:
    def __init__(self, value: Optional[Any] = None, success: bool = True, message: Optional[str] = None):
        self.value = value
        self.success = success
        self.message = message

    def __repr__(self) -> str:
        return f"{self.value or '<no result>'}\n" \
               f"{self.success or 'message'}\n " \
               f"{self.message or 'OK'}\n"

    @staticmethod
    def unit(value):
        return WorkflowBase(value)

    @staticmethod
    def start():
        raise Exception("Not implemented")

    def bind(self, f: Callable[[Any], Any]):
        raise Exception("Not implemented")

    def __rshift__(self, other):
        return self.bind(other)


class WorkflowResult(WorkflowBase):
    def __init__(self, value: Optional[WorkflowData] = None, success: bool = True, message: Optional[str] = None):
        super().__init__(value=value, success=success, message=message)

    @staticmethod
    def unit(value):
        return WorkflowResult(value=value)

    def bind(self, f: Callable[[Any], WorkflowResult]):
        if not self.success:
            return self
        try:
            result = f(self.value)
            return WorkflowResult(
                value=WorkflowData.merge(self.value, result.value),
                success=result.success and self.success,
                message=result.message or ""
            )

        except Exception as exception:
            return WorkflowResult(value=self.value, success=False, message=str(exception))


def read_source_step(value: WorkflowData):
    file_name = value.config["input_file"]
    return WorkflowResult(value=WorkflowData(entries=read_input(file_name)))


def read_config_step(_: Any):
    return WorkflowResult(value=WorkflowData(config=read_config("cfg/config.ini")))


if __name__ == '__main__':
    main = WorkflowResult().unit(None) >> read_config_step >> read_source_step

    print(main)
