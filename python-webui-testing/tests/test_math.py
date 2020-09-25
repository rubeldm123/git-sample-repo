import pytest

@pytest.mark.parametrize(
    "a,b,expected",
    [(0,5,0), (1,5,5), (2,5,10)]

)

def test_multiplication(a, b, expected):
    assert a * b ==expected

test_multiplication    