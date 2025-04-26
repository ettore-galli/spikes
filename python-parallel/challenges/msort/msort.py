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


def merge_sort(array: List[ListElement]) -> List[ListElement]:
    return do_merge_sort(array)
