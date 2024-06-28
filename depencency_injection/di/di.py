from abc import ABC
from dataclasses import dataclass, field
from typing import Dict, Type


@dataclass
class DependencyInjectionManager:
    di_map: Dict[Type[ABC], Type] = field(default_factory=dict)

    def add_config(self, interface: Type[ABC], concrete: Type) -> None:
        self.di_map[interface] = concrete

    def resolve(self, interface: Type[ABC]) -> Type:
        return self.di_map[interface]
