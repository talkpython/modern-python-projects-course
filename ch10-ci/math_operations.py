def add(left, right):
    """Add two numbers.

    >>> from math_operations import add
    >>> add(2, 2)
    4
    >>> add(-1, -1)
    -2

    :param left: augend (left operand)
    :param right: addend (right operand)
    :return: sum of left and right operands
    """
    return left + right


def subtract(left, right):
    """Subtract two numbers.

    >>> from math_operations import subtract
    >>> subtract(2, 2)
    0
    >>> subtract(-3, -1)
    -2

    :param left: minuend (left operand)
    :param right: subtrahend (right operand)
    :return: difference between left and right operand
    """
    return left - right


def multiply(left, right):
    """Multiply two numbers.

    :param left: multiplicand (left operand)
    :param right: multiplier (right operand)
    :return: product of multiplication
    """
    return left * right


def divide(left, right):
    """Divide two numbers."""
    return left // right
