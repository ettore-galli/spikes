"""Calcolatrice RPN feature tests."""

from decimal import Decimal
from pytest import fixture
from pytest_bdd import (
    given,
    scenario,
    then,
    when,
)

from bdd.rpn_calc.rpn_calc import RPNCalc


@scenario("../features/calcolatrice.feature", "Esecuzione di una somma")
def test_add():
    """Esecuzione di una somma."""
    pass


@given("Lo stack è vuoto", target_fixture="calcolatrice")
def calcolatrice():
    """Lo stack è vuoto."""
    calc = RPNCalc()
    calc.clear()
    return calc


@when("Immetto 2")
def enter_first_number(calcolatrice: RPNCalc):
    """Immetto 2."""
    calcolatrice.enter("2")


@when("Immetto 3")
def enter_second_number(calcolatrice: RPNCalc):
    """Immetto 3."""
    calcolatrice.enter("3")


@when("Premo il tasto +")
def add(calcolatrice: RPNCalc):
    """Premo il tasto +."""
    calcolatrice.sum()


@then("Viene mostrato il risultato 5")
def result(calcolatrice: RPNCalc):
    """Viene mostrato il risultato 5."""
    assert calcolatrice.result() == Decimal("5")
