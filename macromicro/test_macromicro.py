from macromicro.macromicro import render_splitted_macros, expected, data, threshold


def test_render_splitted_macros():
    allresult = list(render_splitted_macros(data_macro=data["macro"], threshold=threshold))
    assert [allresult] == expected
