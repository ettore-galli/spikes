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


def calculate_record_scores(
    feature_frequencies: FeatureFrequencyTree, today: Dict[str, str]
) -> Dict[str, float]:
    response_scores = {
        response: {feature: 1 for feature, x in single_feature_frequencies.items()}
        for response, single_feature_frequencies in feature_frequencies.items()
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

    today = {
        "Outlook": "Sunny",
        "Temperature": "Hot",
        "Humidity": "Normal",
        "Windy": "False",
    }

    freqs = {
        "Outlook": {
            "Yes": {
                "Sunny": 0.3333333333333333,
                "Rainy": 0.2222222222222222,
                "Overcast": 0.4444444444444444,
            },
            "No": {"Sunny": 0.4, "Rainy": 0.6, "Overcast": 0.0},
        },
        "Temperature": {
            "Yes": {
                "Hot": 0.2222222222222222,
                "Mild": 0.4444444444444444,
                "Cool": 0.3333333333333333,
            },
            "No": {"Hot": 0.4, "Mild": 0.4, "Cool": 0.2},
        },
        "Humidity": {
            "Yes": {"Normal": 0.6666666666666666, "High": 0.3333333333333333},
            "No": {"Normal": 0.2, "High": 0.8},
        },
        "Windy": {
            "Yes": {"False": 0.6666666666666666, "True": 0.3333333333333333},
            "No": {"False": 0.4, "True": 0.6},
        },
    }
    # scores = calculate_record_scores(feature_frequencies=feature_frequencies, today=today)

    print(feature_frequencies)
