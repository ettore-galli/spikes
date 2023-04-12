from __future__ import annotations
from dataclasses import dataclass

from typing import Any, Callable, List, Union


def get_user_input(prompt: str) -> str:
    return input(prompt if prompt is not None else "-->")


def calculate(command: str) -> str:
    return "*" + command + "*"


def output_feedback(result: str) -> None:
    print(result)


RawFunction = Callable[[Any], Any]

StepFunction = Callable[[Any], Any]


@dataclass(frozen=True)
class StepResult:
    success: bool
    payload: Any


def step(raw_function: RawFunction, arg: Any) -> StepFunction:
    try:
        return StepResult(success=True, payload=raw_function(arg))
    except:
        return StepResult(success=False, payload=arg)


def chain_steps(steps: List[StepFunction], input: Any) -> Any:
    return (
        steps[-1](chain_steps(steps[:-1], input)) if len(steps) > 1 else steps[0](input)
    )


def repl_loop():
    while True:
        chain_steps([get_user_input, calculate, output_feedback], "")


if __name__ == "__main__":
    repl_loop()
