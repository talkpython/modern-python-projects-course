from calculator import Calculator


def test_calculator():
    calc = Calculator()
    calc.add(10)
    calc.subtract(5)
    calc.multiply(5)
    assert str(calc) == "Calculator(25)"


def test_calculator_initial_value():
    calc = Calculator(10)
    assert str(calc) == "Calculator(10)"
    calc.add(5)
    assert str(calc) == "Calculator(15)"


def test_chaining_operations():
    calc = Calculator()
    calc.add(5).add(10).subtract(15)
    assert str(calc) == "Calculator(0)"
