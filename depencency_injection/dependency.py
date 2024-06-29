from depencency_injection.reader.reader_base import BaseFileReader
from depencency_injection.reader.fake_reader import FakeDataFileReader

from depencency_injection.di.di import dependency
from depencency_injection.reader.file_reader import DataFileReader


def make_normal_dependency():
    dependency.add_config(BaseFileReader, DataFileReader())


def make_fake_dependency():
    dependency.add_config(BaseFileReader, FakeDataFileReader())
