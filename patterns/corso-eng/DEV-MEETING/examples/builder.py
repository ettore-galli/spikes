from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Optional
from datetime import datetime


class Logger(ABC):
    @abstractmethod
    def set_writer(self, writer: Writer):
        ...

    @abstractmethod
    def set_formatter(self, formatter: Formatter):
        ...

    @abstractmethod
    def log(self, message):
        ...


class Formatter(ABC):
    @abstractmethod
    def format_message(self, message: str) -> str:
        ...


class TextFormatter(ABC):
    def format_message(self, message: str) -> str:
        return f"{datetime.now()}: {message}"


class HtmlFormatter(ABC):
    def format_message(self, message: str) -> str:
        return f"<div><p>Time: {datetime.now()}</p><p>{message}</p></div>"


class Writer(ABC):
    @abstractmethod
    def write_log_message(self, message: str) -> None:
        ...


class ConsoleWriter(ABC):
    def write_log_message(self, message: str) -> None:
        print(message)


class FileWriter(ABC):
    def __init__(self, file) -> None:
        super().__init__()
        self.file = file

    def write_log_message(self, message: str) -> None:
        with open(self.file, "a") as logf:
            logf.write(message + "\n")


class RealLogger(Logger):
    def __init__(
        self,
    ) -> None:
        self.writer: Optional[Writer] = None
        self.formatter: Optional[Formatter] = None

    def set_writer(self, writer: Writer):
        self.writer: Writer = writer

    def set_formatter(self, formatter: Formatter):
        self.formatter: Formatter = formatter

    def log(self, message):
        self.writer.write_log_message(self.formatter.format_message(message=message))


class LoggerBuilder(ABC):
    @abstractmethod
    def set_writer(self, writer: Writer):
        ...

    @abstractmethod
    def set_formatter(self, formatter: Formatter):
        ...

    @abstractmethod
    def get_logger_instance(self):
        ...


class ConsoleTextLoggerBuilder(LoggerBuilder):
    def __init__(self) -> None:
        super().__init__()
        self.product: RealLogger = RealLogger()

    def set_writer(self, writer: Writer):
        self.product.set_writer(writer=writer)

    def set_formatter(self, formatter: Formatter):
        self.product.set_formatter(formatter=formatter)

    def get_logger_instance(self) -> Logger:
        return self.product


class FileTextLoggerBuilder(LoggerBuilder):
    def __init__(self) -> None:
        super().__init__()
        self.product: RealLogger = RealLogger()

    def set_writer(self, writer: Writer):
        self.product.set_writer(writer=writer)

    def set_formatter(self, formatter: Formatter):
        self.product.set_formatter(formatter=formatter)

    def get_logger_instance(self) -> Logger:
        return self.product


class LoggerBuildDirector:
    @classmethod
    def get_text_logger(cls) -> Logger:
        builder = ConsoleTextLoggerBuilder()
        builder.set_formatter(TextFormatter())
        builder.set_writer(ConsoleWriter())
        return builder.get_logger_instance()

    @classmethod
    def get_file_logger(cls, file: str) -> Logger:
        builder = FileTextLoggerBuilder()
        builder.set_formatter(TextFormatter())
        builder.set_writer(FileWriter(file=file))

        return builder.get_logger_instance()


if __name__ == "__main__":
    console_text_logger = LoggerBuildDirector.get_text_logger()
    console_text_logger.log("Hello, text logger!")
    file_logger = LoggerBuildDirector.get_file_logger("data/log.txt")
    file_logger.log("Hello, file logger!")
