# THIS IS A DUMMY CODE THAT WON'T WORK WHEN YOU RUN IT!

# Function
def charge_customer(amount):
    response = Stripe.charge(amount)

    if response.get('status') == "success":
        current_order_status = "processing"
    else:
        display_error_message(response.get('error'))

# Test
def test_payment(monkeypatch):
    # Patch the Stripe.charge() method and make it return "success" status
    monkeypatch.setattr(Stripe, "charge", dict(status="success"))

    # This calls our monkeypatch that always returns "success"
    charge_customer("199")
    assert current_order_status == "processing"
    # ... and so on
