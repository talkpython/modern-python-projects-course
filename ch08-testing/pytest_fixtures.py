import pytest

@pytest.fixture
def authenticated_user():
    user = create_user(email="user@test.com", password="1234")
    authenticate(email="user@test.com", password="1234")
    return user


def test_buy_item(authenticated_user):
    buy_item(authenticated_user, item="Book")
    # ... the rest of the test

def test_admin_permissions(authenticated_user):
    # User can access home page
    assert can_access(authenticated_user, "/") is True
    # User can't access the admin page
    assert can_access(authenticated_user, "admin/") is False
