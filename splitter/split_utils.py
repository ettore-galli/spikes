 
def consumed_space(split_list):
    return sum([1 + len(macro["micro"]) for macro in split_list])


def split_macros(data_macro, threshold):

    split_list = []

    for macro in data_macro:
        residual_micros = macro["micro"]
        while residual_micros:
            append_micros = residual_micros[
                : (threshold - consumed_space(split_list) - 1)
            ]
            residual_micros = residual_micros[len(append_micros) :]
            split_list.append({**macro, "micro": append_micros})
            if threshold - consumed_space(split_list) == 0:
                yield split_list
                split_list = []

    yield split_list


