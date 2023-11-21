from typing import Dict, List, Optional, Tuple, Union

import csv

import numpy as np

import keras

from sklearn import preprocessing
from sklearn.calibration import LabelEncoder


def float_or_none(candidate: str) -> Optional[float]:
    try:
        return float(candidate)
    except ValueError:
        return None


def prepare_row(
    data_row: List[str],
) -> Tuple[Union[float, None, str], ...]:
    return tuple(float_or_none(item) for item in data_row[:-1]) + (data_row[-1],)


def load_incident_rc_data(incident_rc_data_file: str) -> np.ndarray:
    with open(incident_rc_data_file, newline="", encoding="utf-8") as csvfile:
        reader = csv.DictReader(csvfile)
        return np.array([prepare_row(list(row.values())) for row in reader])


def split_features_target(data: np.ndarray) -> Tuple[np.ndarray, np.ndarray]:
    features = data[:, 1:-1]
    target = data[:, -1]
    return features, target


def categorize_target(data: np.ndarray) -> Tuple[np.ndarray, LabelEncoder]:
    label_encoder = preprocessing.LabelEncoder()
    return label_encoder.fit_transform(data)


def categorize_target_np(data: np.ndarray) -> Tuple[np.ndarray, Dict]:
    categories = {category: ordinal for ordinal, category in enumerate(set(data))}
    reverse_map = {value: key for key, value in categories.items()}
    category = np.vectorize(lambda item: categories.get(item, None))

    return category(data), reverse_map


def build_target_categorical(data: np.ndarray) -> np.ndarray:
    return keras.utils.to_categorical(data)


def rescale_input(data: np.ndarray) -> np.ndarray:
    scaler = preprocessing.StandardScaler().fit(data)
    return scaler.transform(data)


# To do:
# def build_target_categorical_np(data: np.ndarray) -> np.ndarray:
#     ...


def prepare_incident_rc_data(incident_rc_data_file: str):
    data = load_incident_rc_data(incident_rc_data_file)
    features, target = split_features_target(data)
    categorized_target, reverse_map = categorize_target_np(target)
    categotical_target = build_target_categorical(categorized_target)
    rescaled_features = rescale_input(features)

    return rescaled_features, categotical_target, reverse_map
