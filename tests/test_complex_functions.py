import pytest
from complex_functions import square, exponent, floor_div

@pytest.mark.parametrize("a, expected", [(2, 4), (4, 16), (5, 25)])
def test_square(a, expected):
    assert expected == square(a)

@pytest.mark.parametrize("a, b, expected", [(2, 3, 8), (3, 2, 9), (4, 3, 64)])
def test_exponent(a, b, expected):
    assert expected == exponent(a, b)

@pytest.mark.parametrize("a, b, expected", [(5, 2, 2), (4, 3, 1), (6, 4, 1)])
def test_floor_div(a, b, expected):
    assert expected == floor_div(a, b)