from ctypes import c_double
import multiprocessing
from typing import List, Union


ListElement = Union[float, int]


def do_merge_sort_merge(
    left: List[ListElement], right: List[ListElement]
) -> List[ListElement]:
    merged = []

    i_left = 0
    i_right = 0

    while i_left < len(left) and i_right < len(right):
        if left[i_left] <= right[i_right]:
            merged.append(left[i_left])
            i_left += 1
        else:
            merged.append(right[i_right])
            i_right += 1

    merged.extend(left[i_left:])
    merged.extend(right[i_right:])

    return merged


def do_merge_sort(array: List[ListElement]) -> List[ListElement]:
    if len(array) > 1:
        mid = len(array) // 2
        left = do_merge_sort(array[:mid])
        right = do_merge_sort(array[mid:])

        return do_merge_sort_merge(left=left, right=right)

    else:
        return array


def do_merge_sort_merge_mp(merged, left, right) -> None:

    i_left = 0
    i_right = 0
    i_merged = 0

    while i_left < len(left) and i_right < len(right):
        if left[i_left] <= right[i_right]:
            merged[i_merged] = left[i_left]
            i_left += 1
        else:
            merged[i_merged] = right[i_right]
            i_right += 1
        i_merged += 1

    while i_left < len(left):
        merged[i_merged] = left[i_left]
        i_left += 1
        i_merged += 1

    while i_right < len(right):
        merged[i_merged] = right[i_right]
        i_right += 1
        i_merged += 1


def do_merge_sort_mp(array, multiprocessing_threshold: int = 100) -> None:

    if len(array) < multiprocessing_threshold:
        array[:] = do_merge_sort(array=array)
        return

    if len(array) > 1:
        mid = len(array) // 2

        left = multiprocessing.RawArray(c_double, array[:mid])
        right = multiprocessing.RawArray(c_double, array[mid:])

        do_merge_sort_mp(
            array=left,
            multiprocessing_threshold=multiprocessing_threshold,
        )

        do_merge_sort_mp(
            array=right,
            multiprocessing_threshold=multiprocessing_threshold,
        )

        do_merge_sort_merge_mp(merged=array, left=left, right=right)


def merge_sort(array: List[ListElement]) -> List[ListElement]:
    return do_merge_sort(array)


def merge_sort_mp(
    array: List[ListElement], multiprocessing_threshold: int = 100
) -> List[ListElement]:
    tosort = multiprocessing.RawArray(c_double, array)

    do_merge_sort_mp(tosort, multiprocessing_threshold=multiprocessing_threshold)
    return tosort[:]
