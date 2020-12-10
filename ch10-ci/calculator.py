from math_operations import add, divide, multiply, subtract


class Calculator:
    """Simple calculator with basic math operations."""

    def __init__(self, value=0):
        """Initialize the value of the calculator."""
        self.value = value

    def __repr__(self):
        """Return the current value."""
        return f"Calculator({self.value})"

    def add(self, operand):
        """Add operand to the current value of the calculator.

        >>> from calculator import Calculator
        >>> calculator = Calculator(5)
        >>> calculator.add(10)
        Calculator(15)
        """
        self.value = add(self.value, operand)
        return self

    def subtract(self, operand):
        self.value = subtract(self.value, operand)
        return self

    def multiply(self, operand):
        self.value = multiply(self.value, operand)
        return self

    def divide(self, operand):
        self.value = divide(self.value, operand)
        return self
