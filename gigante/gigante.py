# [(f"Art. {i+1}", round(4*random.random(), 2)) for i in range(20)]

from decimal import Decimal
from typing import List, Tuple, Union


Value = Union[float, int, Decimal]
Item = Tuple[str, Value]
Combination = List[Item]
ValuedCombination = Tuple[Combination, Value]

ITEMS = [
    ("Art. 1", 2.84),
    ("Art. 2", 1.26),
    ("Art. 3", 3.54),
    ("Art. 4", 2.6),
    ("Art. 5", 0.88),
    ("Art. 6", 2.47),
    ("Art. 7", 3.03),
    ("Art. 8", 2.61),
    ("Art. 9", 0.71),
    ("Art. 10", 2.38),
    ("Art. 11", 2.25),
    ("Art. 12", 2.24),
    ("Art. 13", 3.7),
    ("Art. 14", 2.95),
    ("Art. 15", 2.89),
    ("Art. 16", 3.27),
    ("Art. 17", 3.86),
    ("Art. 18", 2.16),
    ("Art. 19", 0.95),
    ("Art. 20", 3.82),
]


def combinations(source: List[Item], number: int):
    if number > 0:
        return [
            [current] + combi
            for (c, current) in enumerate(source)
            for combi in combinations(
                [item for (i, item) in enumerate(source) if item != current and i > c],
                number - 1,
            )
        ]
    else:
        return [[]]


def value_combination(combination: Combination) -> ValuedCombination:
    return combination, sum(item[1] for item in combination)


def value_combinations(combinations: List[Combination]) -> List[ValuedCombination]:
    return [value_combination(combi) for combi in combinations]


def select_combinations(
    valued_combinations: List[ValuedCombination], threshold: Value
) -> List[ValuedCombination]:
    return [
        combi for combi in valued_combinations if threshold < combi[1] < threshold * 1.2
    ]


if __name__ == "__main__":
    for n in range(2, len(ITEMS)):
        for combi in select_combinations(
            value_combinations(combinations(ITEMS, n)), 15
        ):
            print("---")
            print(combi)
