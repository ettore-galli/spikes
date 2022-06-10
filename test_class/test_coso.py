from unittest import mock
import pytest
from test_class.coso import CosoBase, CosoSpecifico


def myinit(self, *_):
    [self.a, self.b, self.c, self.qwerty] = [1, 1, 1, 42]


# https://stackoverflow.com/questions/27907356/mock-superclass-init-method-or-superclass-as-a-whole-for-testing
@mock.patch("test_class.coso.CosoBase.__init__", autospec=True, return_value=None)
def test_coso_specifico(_):

    cs = CosoSpecifico(1, 2, 3)
    cs.a = 1
    cs.b = 1
    cs.c = 1
    cs.qwerty = 42
    cs.descrivi = lambda: "Sono Finto?"
    assert cs.descrivi() == "Sono Finto?"
