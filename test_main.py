"""
Test goes here

"""

from mylib.calculator import add, subtract, multiply, divide


def test_add():
    assert add(1, 2) == 3


# create a multiply test
def test_multiply():
    assert multiply(2, 3) == 6


# create a subtract test
def test_subtract():
    assert subtract(3, 2) == 1


# create a divide test
def test_divide():
    assert divide(4, 2) == 2
