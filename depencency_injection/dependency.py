from depencency_injection.reader.reader_base import BaseFileReader
from depencency_injection.reader.file_reader import DataFileReader

from depencency_injection.di.di import DependencyInjectionManager


dependency = DependencyInjectionManager()
dependency.add_config(BaseFileReader, DataFileReader)
