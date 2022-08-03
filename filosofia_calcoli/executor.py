import os


def execute_module(name: str):

    filename = os.path.join(os.path.dirname(__file__), f"{name}.py")

    try:
        with open(filename, "r") as calc_module:
            compiled = compile(calc_module.read(), filename, "exec")
            environment = {
                "thresholds": {"a": 1, "b": 2},
                "inputs": {"x": 11, "y": 22},
                "result": None,
            }

            exec(compiled, {}, environment)

            print(environment["result"])
            print(environment)
    except Exception as error:
        print(error)
        return -1


if __name__ == "__main__":
    execute_module("m1")
