"""Tests for `aida_retreat_24` package."""

import pytest

from aida_retreat_24.main import fibonacci


def test_fibonacci_case_zero():
    """This code is a test case for the Fibonacci function.

    It is checking if the function correctly returns 0 when the input is 0.

    It uses the assert statement to compare the result of calling the fibonacci function with 0 as an argument,
    to the expected value of 0.

    The purpose of this test case is to ensure that the fibonacci function behaves as expected for the edge case of 0.

    To run this test case, the fibonacci function needs to be defined and available in the current scope.

    Example usage:
        fibonacci(0) == 0

    """
    assert fibonacci(0) == 0


def test_fibonacci_case_one():
    """This is a test case for the `fibonacci` function.

    Returns:
        None

    Raises:
        AssertionError: If the `fibonacci` function does not return the expected result.
    """
    assert fibonacci(1) == 1


def test_fibonacci_case_two():
    """This function tests the functionality of the fibonacci() function with an input of 2.

    It asserts that the fibonacci() function will return the expected output, which is 1.

    Example usage:
        test_fibonacci_case_two()
    """
    assert fibonacci(2) == 1


def test_fibonacci_case_positive():
    """This function tests the Fibonacci function with positive test cases.

    Parameters:
    - None

    Returns:
    - None

    Raises:
    - AssertionError: If any of the test cases fail.
    """
    assert fibonacci(5) == 5
    assert fibonacci(10) == 55


def test_fibonacci_case_negative():
    """This function is a test case for the `fibonacci` function to handle negative input.

    Parameters:
    - None

    Returns:
    - None

    Raises:
    - `ValueError` if the `fibonacci` function is called with a negative number as input.

    Example Usage:
    ```
    test_fibonacci_case_negative()
    ```
    """
    with pytest.raises(ValueError):
        fibonacci(-1)
