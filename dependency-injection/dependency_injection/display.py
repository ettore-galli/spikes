from dependency_injection.process import (
    display_file_content_injected,
    display_file_content_process,
)


def display(file: str):
    display_file_content_process(file=file)
    display_file_content_injected(file=file) 
