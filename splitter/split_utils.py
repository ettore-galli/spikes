from typing import Any, Callable, Iterable, List, Tuple


def consumed_space(split_list):
    return sum([1 + len(macro["micro"]) for macro in split_list])


def split_macros(data_macro, threshold):

    split_list = []

    for macro in data_macro:
        residual_micros = macro["micro"]
        while residual_micros:
            append_micros = residual_micros[
                : (threshold - consumed_space(split_list) - 1)
            ]
            residual_micros = residual_micros[len(append_micros) :]
            split_list.append({**macro, "micro": append_micros})
            if threshold - consumed_space(split_list) == 0:
                yield split_list
                split_list = []

    yield split_list


ObjectToSplit = Any
ObjectElement = Any
ObjectSize = int
ElementSize = int


def element_consumed_space(container_object: ObjectToSplit) -> ObjectSize:
    return 1 + len(container_object["micro"])


def structure_consumed_space(split_list: Iterable[ObjectToSplit]) -> ObjectSize:
    return sum([element_consumed_space(container_object=macro) for macro in split_list])


def all_elements(container_object: ObjectToSplit) -> List[ObjectElement]:
    return container_object["micro"]


def new_with_elements(
    container_object: ObjectToSplit, append_elements: List[ObjectElement]
) -> ObjectToSplit:
    return {**container_object, "micro": append_elements}


def split_by_space(
    data: Iterable[ObjectToSplit],
    space_threshold: ObjectSize,
):

    split_list = []

    for container_object in data:
        residual_elements = all_elements(container_object)
        while residual_elements:
            append_elements = residual_elements[
                : (space_threshold - structure_consumed_space(split_list) - 1)
            ]
            residual_elements = residual_elements[len(append_elements) :]
            split_list.append(new_with_elements(container_object, append_elements))
            if space_threshold - structure_consumed_space(split_list) == 0:
                yield split_list
                split_list = []

    yield split_list
