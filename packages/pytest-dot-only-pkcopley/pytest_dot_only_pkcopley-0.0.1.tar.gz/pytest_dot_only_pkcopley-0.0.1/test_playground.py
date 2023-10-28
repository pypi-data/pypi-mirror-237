from playground import add
import pytest


def test_add_ones():
    assert add(1, 1) == 2


@pytest.mark.only
def test_add_twos():
    assert add(2, 2) == 4


def test_add_threes():
    assert add(3, 3) == 6
