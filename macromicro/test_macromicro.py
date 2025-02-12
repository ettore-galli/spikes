from macromicro.macromicro import render_splitted, expected, data, threshold


def test_render_splitted():
    allresult = list(render_splitted(data_macro=data["macro"], threshold=threshold))
    assert [allresult] == expected
