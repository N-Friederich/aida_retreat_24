

def fibonacci(n: int = 5) -> int:
    """
    Calculate the Fibonacci sequence for a given number.

    Args:
        n: The number for which the Fibonacci sequence needs to be calculated. Defaults to 5.

    Returns:
        The nth number in the Fibonacci sequence.

    Raises:
        ValueError: If n is a negative integer.

    """

    if n < 0:
        raise ValueError("n must be a positive integer")

    elif n == 0:
        return 0

    elif n == 1 or n == 2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
