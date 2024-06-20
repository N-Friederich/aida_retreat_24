import pytest
from aida_retreat_24.main import fibonacci


def test_fibonacci_case_zero():
    assert fibonacci(0) == 0


def test_fibonacci_case_one():
    assert fibonacci(1) == 1


def test_fibonacci_case_two():
    assert fibonacci(2) == 1


def test_fibonacci_case_positive():
    assert fibonacci(5) == 5
    assert fibonacci(10) == 55


def test_fibonacci_case_negative():
    with pytest.raises(ValueError):
        fibonacci(-1)