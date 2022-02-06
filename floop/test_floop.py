from typing import List

from floop.floop import floop


def make_consumer(expected_data_windows: List[any]):

    class ConsumerBase():
        def __init__(self, expected_data_windows):
            self.index = 0
            self.expected_data_windows = expected_data_windows

        def __call__(self, data_window):
            assert data_window == expected_data_windows[self.index]
            self.index +=1

    return ConsumerBase(expected_data_windows)


def test_floop():
    source = [f"e{n}" for n in range(20)]
    expected_data_windows = [
        ["e0"],
        ["e0", "e1"],
        ["e0", "e1", "e2"],
        ["e1", "e2", "e3"],
        ["e2", "e3", "e4"],
        ["e3", "e4", "e5"],
        ["e4", "e5", "e6"],
        ["e5", "e6", "e7"],
        ["e6", "e7", "e8"],
        ["e7", "e8", "e9"],
        ["e8", "e9", "e10"],
        ["e9", "e10", "e11"],
        ["e10", "e11", "e12"],
        ["e11", "e12", "e13"],
        ["e12", "e13", "e14"],
        ["e13", "e14", "e15"],
        ["e14", "e15", "e16"],
        ["e15", "e16", "e17"],
        ["e16", "e17", "e18"],
        ["e17", "e18", "e19"],
    ]

    floop(source, make_consumer(expected_data_windows), data_window_length=3)
