from abc import ABC
from dataclasses import dataclass, field
from functools import wraps
from typing import Any, Callable, Dict, List, Type


@dataclass
class DependencyInjectionManager:
    di_map: Dict[Type[ABC], Type] = field(default_factory=dict)

    def add_config(self, interface: Type[ABC], concrete: Type) -> None:
        self.di_map[interface] = concrete

    def resolve(self, interface: Type[ABC]) -> Type:
        return self.di_map[interface]

    def can_resolve(self, interface: Type[ABC]) -> bool:
        return interface in self.di_map

    def retrieve_injectable_parameters(self, injectand: Callable) -> List:
        return list(injectand.__annotations__.items())

    def inject_dependencies(self, injectand: Callable) -> Callable:
        @wraps(injectand)
        def injected_function(*args, **kwargs):
            injected_parameters: Dict = {
                parameter_name: dependency.resolve(parameter_type)
                for parameter_name, parameter_type in self.retrieve_injectable_parameters(
                    injectand=injectand
                )
                if dependency.can_resolve(parameter_type)
            }
            residual_kwargs = {
                arg: value
                for arg, value in kwargs.items()
                if arg not in injected_parameters
            }
            residual_args = [arg for arg in args if arg not in injected_parameters]
            return injectand(
                *residual_args, **{**residual_kwargs, **injected_parameters}
            )

        return injected_function


dependency = DependencyInjectionManager()


class perform_injection:
    def __init__(self, injectand: Callable) -> None:
        @wraps(injectand)
        def injected_function(*args, **kwargs):
            injected_parameters: Dict = {
                parameter_name: dependency.resolve(parameter_type)
                for parameter_name, parameter_type in dependency.retrieve_injectable_parameters(
                    injectand=injectand
                )
                if dependency.can_resolve(parameter_type)
            }
            residual_kwargs = {
                arg: value
                for arg, value in kwargs.items()
                if arg not in injected_parameters
            }
            residual_args = [arg for arg in args if arg not in injected_parameters]
            return injectand(
                *residual_args, **{**residual_kwargs, **injected_parameters}
            )

        self.injected_function = injected_function

    def __call__(self, *args: Any, **kwds: Any) -> Any:
        return self.injected_function(*args, **kwds)
