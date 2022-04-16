from typing import Optional, Any, Callable


class WorkflowResult:
    def __init__(self, value: Optional[Any] = None, success: bool = True, error: Optional[str] = None):
        self.value = value
        self.success = success
        self.error = error

    def __repr__(self) -> str:
        return f"{self.value or '<no result>'}, {self.success or 'ERROR'}, {self.error or 'OK'}\n"

    @staticmethod
    def unit(value):
        return WorkflowResult(value)

    @staticmethod
    def start():
        return WorkflowResult.unit(0)

    def bind(self, f: Callable[[Any], Any]):
        if not self.success:
            return self
        try:
            return WorkflowResult(f(self.value))
        except Exception as error:
            return WorkflowResult(value=None, success=False, error=str(error))

    def __rshift__(self, other):
        return self.bind(other)


def read_source():
    pass

if __name__ == '__main__':
    cr = WorkflowResult(42)
    ce = WorkflowResult(success=False, error="Booooo")


    start = (lambda: 100)()
    div_2 = lambda x: x / 2
    add_input = lambda x: x + float(input("? "))
    scale_up = lambda x: x * 100000


    def log_status(x):
        print(f"->{x}")
        return x


    # main = CalculationResult.unit(start) >> log_status >> div_2 >> log_status >> add_input >> log_status >> scale_up
    main = WorkflowResult.start() >> add_input >> log_status >> div_2 >> log_status >> add_input >> log_status >> scale_up

    print(main)
