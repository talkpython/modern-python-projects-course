import pytest

@pytest.mark.parametrize(
    "left,right,output",
    [
        (1, 1, 2),
        (10, 100, 110),
        (1, -10, -9),
        (-10, -10, -10),
    ]
)
def test_add_numbers(left, right, output):
    assert left + right == output
