from depencency_injection.process import display_file_content

from depencency_injection.di.di import dependency
from depencency_injection.reader.reader_base import BaseFileReader


def display(file: str):
    display_file_content(file_reader=dependency.resolve(BaseFileReader), file=file)
