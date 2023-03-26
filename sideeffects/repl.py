from __future__ import annotations

from typing import Any, Callable, Union


def get_user_input(prompt: str) -> str:
    return input(prompt if prompt is not None else "-->")


def calculate(command: str) -> str:
    return "*" + command + "*"


def output_feedback(result: str) -> None:
    print(result)

StepFunction = Callable[[Any], Any]

class Step:
    def __init__(self, step_function: StepFunction, data: Any = None) -> None:
        self.step_function = step_function
        self.data = data

    def concat(self, next_step: Union[Step, StepFunction] = lambda x: x) -> Step:
        if isinstance(next_step, Step):
            return Step(next_step.step_function, self.step_function(self.data))  
        return Step(next_step, self.step_function(self.data))  


def main_loop():
    Step(step_function=get_user_input).concat(calculate).concat(
        output_feedback
    ).concat()
    
    input = Step(step_function=get_user_input)

    processed = input.concat(calculate)

    feedback = processed.concat(output_feedback)

    feedback.concat(input)


if __name__ == "__main__":
    main_loop()
