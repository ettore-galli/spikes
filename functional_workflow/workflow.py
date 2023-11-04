from __future__ import annotations

import os
from typing import (
    List,
    Optional,
    Any,
    Callable,
    Dict,
)

from dataclasses import dataclass, field

from functional_workflow.config import read_config
from functional_workflow.logger import log
from functional_workflow.reader import read_input
from functional_workflow.writer import write_output


@dataclass
class WorkflowStep:
    payload: Optional[Any] = None
    config: Dict = field(default_factory=dict)
    success: bool = True
    issues: List[str] = field(default_factory=list)

    @staticmethod
    def unit() -> WorkflowStep:
        return WorkflowStep()

    def bind(
        self,
        f: StepFunction,
    ) -> WorkflowStep:
        if not self.success:
            return self
        try:
            result: WorkflowStep = f(self)

            return WorkflowStep(
                config=self.config or result.config,
                success=self.success and result.success,
                payload=result.payload if result.success else self.payload,
                issues=self.issues + result.issues,
            )

        except Exception as exception:
            return WorkflowStep(
                config=self.config,
                payload=self.payload,
                success=False,
                issues=self.issues + [str(exception)],
            )

    def __repr__(self) -> str:
        return (
            "Workflow Result:"
            f"\n - Payload : {str(self.payload) or '<no payload>'}"
            f"\n - Success : {self.success} "
            f"\n - Issues : {self.issues or ['OK']}"
        )

    def __rshift__(self, other):
        return self.bind(other)


StepFunction = Callable[[WorkflowStep], WorkflowStep]


def read_config_step(_: WorkflowStep) -> WorkflowStep:
    return WorkflowStep(config=read_config("cfg/config.ini"))


def read_source_step(prv: WorkflowStep) -> WorkflowStep:
    file_name = prv.config["input_file"]
    return WorkflowStep(payload=read_input(file_name))


def log_current_step(prv: WorkflowStep) -> WorkflowStep:
    log(f"--> Processing: {str(prv.payload)}")
    return prv


def compose_output_file_name(entry: str, config: Dict):
    return os.path.join(
        config["output_directory"],
        f'{config["output_file_prefix"]}_{entry[:10].strip()}.txt',
    )


def write_output_step(prv: WorkflowStep) -> WorkflowStep:
    for entry_data in prv.payload:
        output_file_name = compose_output_file_name(entry_data, prv.config)
        write_output(entry_data, output_file_name)

    return prv


if __name__ == "__main__":
    main = (
        WorkflowStep.unit() >> read_config_step >> read_source_step >> write_output_step
    )

    print(main)
