from macromicro.macromicro import (
    render_splitted_lists,
    expected,
    data,
    split_macros,
    threshold,
)


def test_render_splitted_lists():
    allresult = list(
        render_splitted_lists(data_macro=data["macro"], threshold=threshold)
    )
    assert allresult == expected


def test_split_macros():
    allresult = list(split_macros(data_macro=data["macro"], threshold=threshold))
    assert allresult == expected
