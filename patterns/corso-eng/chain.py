from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Optional


class Configuration(ABC):
    def __init__(self) -> None:
        super().__init__()
        self.next_processor: Optional[Configuration] = None

    @abstractmethod
    def set_next_processor(self, cfg: Configuration):
        ...

    @abstractmethod
    def get_configuration(self) -> str:
        ...


class BaseConfiguration(Configuration):
    def set_next_processor(self, next_processor: Configuration):
        self.next_processor = next_processor

    def delegate(self):
        return self.next_processor.get_configuration()


class CommandLineConfiguration(BaseConfiguration):
    def get_configuration(self) -> str:
        data = input()
        if len(data) == 0:
            return self.delegate()
        return data


class FileConfiguration(BaseConfiguration):
    def get_configuration(self) -> str:
        data = ""
        with open("data/config.txt") as cfg:
            data = cfg.read()

        if len(data) == 0:
            return self.delegate()
        return data


class DefaultConfiguration(BaseConfiguration):
    def get_configuration(self) -> str:
        data = "Default"
        if len(data) == 0:
            return self.delegate()
        return data


def config_retriever() -> Configuration:
    cmd_config = CommandLineConfiguration()
    file_config = FileConfiguration()
    default_config = DefaultConfiguration()
    cmd_config.set_next_processor(file_config)
    file_config.set_next_processor(default_config)

    return cmd_config


def application():
    config: Configuration = config_retriever()

    print(config.get_configuration())


if __name__ == "__main__":
    application()
