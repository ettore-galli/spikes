from __future__ import annotations
from split_utils import split_macros

from test_split_utils import data, threshold

if __name__ == "__main__":
    allresult = list(split_macros(data_macro=data["macro"], threshold=threshold))
    print(allresult)
