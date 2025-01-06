from typing import List, Dict

import csv


def load_data(file_fqn: str) -> List[Dict]:
    with open(file_fqn, encoding="utf-8") as csvfile:
        reader = csv.reader(csvfile, delimiter="|")
        return [row for row in reader]

    return []


if __name__ == "__main__":
    print(load_data("statistics/bayes/data/golf.csv"))
