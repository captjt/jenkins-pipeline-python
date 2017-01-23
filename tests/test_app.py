from app.functions import (
    add,
    divide,
    multiply,
    subtract,
)

import pytest


def test_add():
    assert add(4, 5) == 9
    assert add(1, 1) == 2
    assert add(0, 0) == 0
    assert add(-1, 3) == 2

def test_divide():
    assert divide(2, 1) == 2
    assert divide(1, 1) == 1
    assert divide(-10, 5) == -2

def test_multiply():
    assert multiply(2, 2) == 4
    assert multiply(1, 5) == 5
    assert multiply(-10, -10) == 100

def test_subtract():
    assert subtract(10, 9) == 1
    assert subtract(5, 6) == -1
    assert subtract(7, 0) == 7
