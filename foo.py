import pytest

def add_one(x: int) -> int:
    """ 
    Returns its integer argument plus one
    """
    assert isinstance(x, int)
    return x + 1

def test_ok():
    assert add_one(0) == 1
    assert add_one(2) == 3
    assert add_one(-1) == 0

def test_ko():
    with pytest.raises(AssertionError):
        add_one(1.0)
    with pytest.raises(AssertionError):
        add_one({})
    with pytest.raises(AssertionError):
        add_one("foo")
