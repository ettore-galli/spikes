from functools import reduce
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


def get_response_counts(
    feature_counts: FeatureCountTree, response_feature: str
) -> Dict[str, int]:
    return {
        feature: subcount[feature]
        for feature, subcount in feature_counts[response_feature].items()
    }


def compute_conditional_feature_frequencies(
    feature_counts: FeatureCountTree,
    response_feature: str,
    response_counts: Dict[str, int],
) -> Dict[str, Dict[str, float]]:

    conditional_feature_frequencies = {
        feature: {
            response: {
                single_feature: single_feature_count / count
                for single_feature, single_feature_count in counts[response].items()
            }
            for response, count in response_counts.items()
        }
        for feature, counts in feature_counts.items()
        if feature != response_feature
    }

    reclassified_frequences = {
        response: {
            feature: freqs[response]
            for feature, freqs in conditional_feature_frequencies.items()
        }
        for response in response_counts.keys()
    }

    return reclassified_frequences


def calculate_record_features(
    feature_frequencies: FeatureFrequencyTree, today: Dict[str, str]
) -> Dict[str, Dict[str, float]]:
    record_features = {
        response: {
            today_feature: response_frequencies[today_feature][today_value]
            for today_feature, today_value in today.items()
        }
        for response, response_frequencies in feature_frequencies.items()
    }
    return record_features


def calculate_response_scores(
    record_feaures: Dict[str, Dict[str, float]],
    response_counts: Dict[str, int],
) -> Dict[str, float]:
    response_scores = {
        response: response_counts[response]
        * reduce(lambda acc, cur: acc * cur, response_frequencies.values(), 1)
        for response, response_frequencies in record_feaures.items()
    }
    return response_scores


def classify_record(
    feature_frequencies: FeatureFrequencyTree,
    response_counts: Dict[str, int],
    today: Dict[str, str],
) -> Dict[str, float]:
    return calculate_response_scores(
        record_feaures=calculate_record_features(
            feature_frequencies=feature_frequencies, today=today
        ),
        response_counts=response_counts,
    )


if __name__ == "__main__":
    data = load_data("statistics/bayes/data/golf.csv")
    features = ["Outlook", "Temperature", "Humidity", "Windy", "PlayGolf"]
    response_feature = "PlayGolf"

    feature_count = compute_feature_count(
        data=data, features=features, response_feature=response_feature
    )
    response_counts = get_response_counts(feature_count, "PlayGolf")

    feature_frequencies = compute_conditional_feature_frequencies(
        feature_count, "PlayGolf", response_counts
    )

    today = {
        "Outlook": "Sunny",
        "Temperature": "Hot",
        "Humidity": "Normal",
        "Windy": "False",
    }
    example2 = {
        "Outlook": "Sunny",
        "Temperature": "Mild",
        "Humidity": "Normal",
        "Windy": "False",
    }

    classification = classify_record(
        feature_frequencies=feature_frequencies,
        response_counts=response_counts,
        today=today,
    )

    print(classification)

    classification = classify_record(
        feature_frequencies=feature_frequencies,
        response_counts=response_counts,
        today=example2,
    )

    print(classification)  # 0470223585118    letixmail@gmail.com 3385973451

    # 051 19937469

    
