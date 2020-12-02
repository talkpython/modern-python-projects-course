import pytest

@pytest.mark.parametrize(
    "number_of_items,expected_cart_size",
    [
        (1, 1),
        (10, 10),
        (-1, 0),
    ]
)
def test_add_items_to_cart(number_of_items,expected_cart_size):
    cart = Cart()
    cart.add_item("Book", number_of_items=number_of_items)
    assert cart.size == expected_cart_size
