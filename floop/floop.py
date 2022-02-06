"""
Functional Universal Looper

Given a data source, calls a consumer funcion
providing a data window of a number of specified elements

"""
from typing import List, Callable


def floop(
    source: List[any],
    consumer: Callable[[List[any]], None],
    data_window_length: int = 2,
):

    data_window = []
    for element in source:
        data_window = (
            data_window[-(data_window_length - 1) :] + [element]
            if data_window_length > 0
            else [element]
        )
        consumer(data_window)



