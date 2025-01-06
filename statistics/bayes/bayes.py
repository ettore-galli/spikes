from typing import List, Dict

import csv

FeatureCountTree = Dict[str, Dict[str, Dict[str, int]]]
FeatureFrequencyTree = Dict[str, Dict[str, float]]


def load_data(file_fqn: str) -> List[Dict]:
    with open(file_fqn, encoding="utf-8") as csvfile:
        reader = csv.DictReader(csvfile, delimiter="|")
        return [row for row in reader]

    return []


def compute_feature_count(
    data: List[Dict], features: List[str], response_feature: str
) -> FeatureCountTree:

    feature_counts: Dict[str, Dict[str, Dict[str, float]]] = {}

    response_values = set([row[response_feature] for row in data])

    for attribute in features:
        distinct_values = set([row[attribute] for row in data])

        frequencies = {
            response_value: {
                value: len(
                    [
                        row
                        for row in data
                        if row[attribute] == value
                        if row[response_feature] == response_value
                    ]
                )
                for value in distinct_values
            }
            for response_value in response_values
        }
        feature_counts[attribute] = frequencies

    return feature_counts


def compute_conditional_feature_frequencies(
    feature_counts: FeatureCountTree, response_feature: str
) -> Dict[str, Dict[str, float]]:
    response_counts = {
        feature: subcount[feature]
        for feature, subcount in feature_counts[response_feature].items()
    }
    return {
        feature: {
            response: {
                single_feature:  single_feature_count/ count
                for single_feature, single_feature_count in counts[response].items()
            }
            for response, count in response_counts.items()
        }
        for feature, counts in feature_counts.items()
    }


if __name__ == "__main__":
    data = load_data("statistics/bayes/data/golf.csv")
    features = ["Outlook", "Temperature", "Humidity", "Windy", "PlayGolf"]
    response_feature = "PlayGolf"

    feature_count = compute_feature_count(
        data=data, features=features, response_feature=response_feature
    )

    feature_frequencies = compute_conditional_feature_frequencies(
        feature_count, "PlayGolf"
    )

    print(feature_frequencies)
