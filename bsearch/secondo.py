from typing import List


def secondo(data: List[int]) -> int:
    return max(item for item in data if item < max(data))


if __name__ == "__main__":
    data = [1, 5, 7, 6, 8, 3, 5, 7]
    print(secondo(data))
