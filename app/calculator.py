"""Pure functions — easy to unit-test, no framework needed."""


def add(a: float, b: float) -> float:
    """Return the sum of two numbers."""
    return a + b


def divide(a: float, b: float) -> float:
    """Return a divided by b. Raises ValueError on divide-by-zero."""
    if b == 0:
        raise ValueError("cannot divide by zero")
    return a / b
