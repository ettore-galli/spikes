from typing import List, Tuple


def twosum(nums: List[int], target: int) -> Tuple[int, int]:
    enumeration = [(idx, num) for idx, num in enumerate(nums)]
    for i, ni in enumeration:
        for j, nj in enumeration:
            if ni + nj == target:
                return i, j


if __name__ == "__main__":
    nrs = [1, 4, 7, 2, 5]

    sums = twosum(nrs, target=11)
    print(sums)
    sums = twosum(nrs, target=6)
    print(sums)
    sums = twosum(nrs, target=7)
    print(sums)
