from depencency_injection.dependency import make_fake_dependency
from depencency_injection.process import display_file_content
from depencency_injection.reader.reader_base import BaseFileReader

from depencency_injection.di.di import dependency

make_fake_dependency()

if __name__ == "__main__":
    display_file_content(
        file_reader=dependency.resolve(BaseFileReader), file="data/sample.txt"
    )
