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


def do_merge_sort_merge_mp(merged, start, mid, end) -> None:

    i_left = 0
    i_right = 0
    i_merged = start

    prev_left = multiprocessing.RawArray(c_double, merged[start:mid])
    prev_right = multiprocessing.RawArray(c_double, merged[mid:end])

    while i_left < len(prev_left) and i_right < len(prev_right):
        if prev_left[i_left] <= prev_right[i_right]:
            merged[i_merged] = prev_left[i_left]
            i_left += 1
        else:
            merged[i_merged] = prev_right[i_right]
            i_right += 1
        i_merged += 1

    while i_left < len(prev_left):
        merged[i_merged] = prev_left[i_left]
        i_left += 1
        i_merged += 1

    while i_right < len(prev_right):
        merged[i_merged] = prev_right[i_right]
        i_right += 1
        i_merged += 1


def do_merge_sort_mp(
    array,
    start_index: int,
    end_index: int,
    multiprocessing_threshold: int = 100,
) -> None:

    if end_index - start_index < multiprocessing_threshold:
        array[start_index:end_index] = do_merge_sort(array=array[start_index:end_index])
    else:

        mid_index = start_index + (end_index - start_index) // 2

        left_proc = multiprocessing.Process(
            target=do_merge_sort_mp,
            args=(array, start_index, mid_index, multiprocessing_threshold),
        )
        left_proc.start()

        do_merge_sort_mp(
            array=array,
            start_index=mid_index,
            end_index=end_index,
            multiprocessing_threshold=multiprocessing_threshold,
        )

        left_proc.join()

        do_merge_sort_merge_mp(
            merged=array, start=start_index, mid=mid_index, end=end_index
        )


def merge_sort(array: List[ListElement]) -> List[ListElement]:
    return do_merge_sort(array)


def merge_sort_mp(
    array: List[ListElement], multiprocessing_threshold: int = 100
) -> List[ListElement]:
    tosort = multiprocessing.RawArray(c_double, array)

    do_merge_sort_mp(
        tosort,
        start_index=0,
        end_index=len(tosort),
        multiprocessing_threshold=multiprocessing_threshold,
    )

    return tosort[:]
