from split_utils import (
    split_by_space,
    split_macros,
)

data = {
    "macro": [
        {
            "ctv": 25151.08,
            "description": "BOND CORPORATE",
            "micro": [
                {
                    "ctv": 25151.08,
                    "description": "Bond Corporate Europe HY",
                    "weight": 12.431615458353996,
                }
            ],
            "weight": 12.431615458353996,
        },
        {
            "ctv": 45313.66,
            "description": "BOND GOVERNMENT",
            "micro": [
                {
                    "ctv": 35307.48,
                    "description": "Bond Government Italy",
                    "weight": 17.451696474406848,
                },
                {
                    "ctv": 10006.18,
                    "description": "Bond Government USA",
                    "weight": 4.945830634989536,
                },
            ],
            "weight": 22.397527109396385,
        },
        {
            "ctv": 50139.14,
            "description": "CASH",
            "micro": [
                {
                    "ctv": 25229.62,
                    "description": "Cash Euro",
                    "weight": 12.470436021053457,
                },
                {
                    "ctv": 24909.52,
                    "description": "Cash USD",
                    "weight": 12.312217761311963,
                },
            ],
            "weight": 24.78265378236542,
        },
        {
            "ctv": 81711.58,
            "description": "EQUITY",
            "micro": [
                {
                    "ctv": 7148.757,
                    "description": "Equity EM Asia",
                    "weight": 3.533470452529925,
                },
                {
                    "ctv": 1736.1267000000003,
                    "description": "Equity EM EMEA",
                    "weight": 0.8581285384715533,
                },
                {
                    "ctv": 1327.6263000000001,
                    "description": "Equity EM Latam",
                    "weight": 0.656215941184129,
                },
                {
                    "ctv": 20840.61,
                    "description": "Equity Europe",
                    "weight": 10.301046692131187,
                },
                {
                    "ctv": 10337.62,
                    "description": "Equity Japan",
                    "weight": 5.109654002714374,
                },
                {
                    "ctv": 40320.84,
                    "description": "Equity North America",
                    "weight": 19.92968802285302,
                },
            ],
            "weight": 40.38820364988419,
        },
    ]
}


threshold = 13

expected = [
    [
        {
            "ctv": 25151.08,
            "description": "BOND CORPORATE",
            "micro": [
                {
                    "ctv": 25151.08,
                    "description": "Bond Corporate Europe HY",
                    "weight": 12.431615458353996,
                }
            ],
            "weight": 12.431615458353996,
        },
        {
            "ctv": 45313.66,
            "description": "BOND GOVERNMENT",
            "micro": [
                {
                    "ctv": 35307.48,
                    "description": "Bond Government Italy",
                    "weight": 17.451696474406848,
                },
                {
                    "ctv": 10006.18,
                    "description": "Bond Government USA",
                    "weight": 4.945830634989536,
                },
            ],
            "weight": 22.397527109396385,
        },
        {
            "ctv": 50139.14,
            "description": "CASH",
            "micro": [
                {
                    "ctv": 25229.62,
                    "description": "Cash Euro",
                    "weight": 12.470436021053457,
                },
                {
                    "ctv": 24909.52,
                    "description": "Cash USD",
                    "weight": 12.312217761311963,
                },
            ],
            "weight": 24.78265378236542,
        },
        {
            "ctv": 81711.58,
            "description": "EQUITY",
            "micro": [
                {
                    "ctv": 7148.757,
                    "description": "Equity EM Asia",
                    "weight": 3.533470452529925,
                },
                {
                    "ctv": 1736.1267000000003,
                    "description": "Equity EM EMEA",
                    "weight": 0.8581285384715533,
                },
                {
                    "ctv": 1327.6263000000001,
                    "description": "Equity EM Latam",
                    "weight": 0.656215941184129,
                },
                {
                    "ctv": 20840.61,
                    "description": "Equity Europe",
                    "weight": 10.301046692131187,
                },
            ],
            "weight": 40.38820364988419,
        },
    ],
    [
        {
            "ctv": 81711.58,
            "description": "EQUITY",
            "micro": [
                {
                    "ctv": 10337.62,
                    "description": "Equity Japan",
                    "weight": 5.109654002714374,
                },
                {
                    "ctv": 40320.84,
                    "description": "Equity North America",
                    "weight": 19.92968802285302,
                },
            ],
            "weight": 40.38820364988419,
        }
    ],
]


def test_split_macros():
    allresult = list(split_macros(data_macro=data["macro"], threshold=threshold))
    assert allresult == expected


def test_split_by_space():
    allresult = list(split_by_space(data=data["macro"], space_threshold=threshold))
    assert allresult == expected
