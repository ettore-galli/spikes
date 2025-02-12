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


def render_splitted_macros(data_macro, threshold):
    chunk = []
    estimated_space = 0
    current_macro = None
    for macro in data_macro:
        if current_macro and macro != current_macro:
            yield {**current_macro, **{"micro": chunk}}
            chunk = []
        if macro != current_macro:
            current_macro = macro
            estimated_space += 1
        for micro_item in current_macro["micro"]:
            estimated_space += 1
            chunk.append(micro_item)
            if estimated_space == threshold:
                yield {**current_macro, **{"micro": chunk}}
                estimated_space = 0
                chunk = []

    yield {**current_macro, **{"micro": chunk}}


def render_splitted_lists(data_macro, threshold):
    splitted_list = []
    consumed_space = 0

    for macro in render_splitted_macros(data_macro, threshold):
        consumed_space += 1 + len(macro["micro"])
        splitted_list.append(macro)
        if consumed_space == threshold:
            yield splitted_list
            splitted_list = []

    yield splitted_list


def split_macros(data_macro, threshold):
    split_list = []
    consumed_space = 0

    for macro in data_macro:
        residual_micros = macro["micro"]
        while residual_micros:
            append_micros = residual_micros[: (threshold - consumed_space - 1)]
            residual_micros = residual_micros[len(append_micros) :]
            split_list.append({**macro, "micro": append_micros})
            consumed_space += 1 + len(append_micros)
            if threshold - consumed_space == 0:
                yield split_list
                split_list = []
                consumed_space = 0

    yield split_list


if __name__ == "__main__":
    allresult = list(
        render_splitted_lists(data_macro=data["macro"], threshold=threshold)
    )
    print(allresult)
