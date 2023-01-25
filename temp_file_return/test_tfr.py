from tfr import create_return


def test_tfr():
    content = create_return().readlines()
    assert content == ["Hello, world!"]
