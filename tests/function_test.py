import pytest
from function import add, multp, div
@pytest.mark.parametrize("a, b, expected", [(2, 3, 5), (1, 4, 5), (5, 2, 7)])
def test_add(a, b, expected):
    assert expected == add(a, b)

@pytest.mark.parametrize("a, b, expected", [(1, 2, 2), (5, 2, 10), (3, 3, 9)])
def test_multp(a, b, expected):
    assert expected == multp(a, b)

@pytest.mark.parametrize("a, b, expected", [(8, 4, 2), (6, 3, 2), (5, 1, 5)])
def test_div(a, b, expected):
    assert expected == div(a, b)