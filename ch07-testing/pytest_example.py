import pytest


def test_upper():
    assert "foo".upper() == "FOO"


def test_isupper():
    assert "FOO".isupper() is True
    assert "Foo".isupper() is False


def test_split():
    s = 'hello world'
    assert s.split() == ['hello', 'world']
    with pytest.raises(TypeError):
        s.split(2)
