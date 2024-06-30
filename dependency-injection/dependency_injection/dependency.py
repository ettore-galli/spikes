from dependency_injection.reader.reader_base import BaseFileReader
from kink import di

from dependency_injection.reader.fake_reader import FakeDataFileReader

from dependency_injection.di.di import dependency
from dependency_injection.reader.file_reader import DataFileReader


def make_normal_dependency():
    dependency.add_config(BaseFileReader, DataFileReader())
    di[BaseFileReader] = DataFileReader()


def make_fake_dependency():
    dependency.add_config(BaseFileReader, FakeDataFileReader())
    di[BaseFileReader] = FakeDataFileReader()
