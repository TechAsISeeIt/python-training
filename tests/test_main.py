import pytest
from src.Training.Basics.static_types_check import add, get_length


# ---------- Tests for add ----------


def test_add_positive_numbers():
    assert add(2, 3) == 5


def test_add_negative_numbers():
    assert add(-1, -2) == -3


def test_add_mixed_numbers():
    assert add(-1, 5) == 4


def test_add_zero():
    assert add(0, 0) == 0


# ---------- Tests for get_length ----------


def test_get_length_valid_string():
    result = get_length("hello")
    assert result == {"length": 5, 1: "hello"}


def test_get_length_single_character():
    result = get_length("a")
    assert result == {"length": 1, 1: "a"}


def test_get_length_empty_string():
    result = get_length("")
    assert result is None


def test_get_length_none_input():
    # This will raise TypeError before your ValueError logic
    with pytest.raises(TypeError):
        get_length(None)  # type: ignore


def test_get_length_special_characters():
    result = get_length("!@#")
    assert result == {"length": 3, 1: "!@#"}
