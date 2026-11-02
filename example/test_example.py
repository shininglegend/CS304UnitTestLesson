"""pytest in one file.

- Any function named test_* in a file named test_*.py is a test.
- A plain `assert` is the check. pytest shows both sides when it fails.
- pytest.raises checks that an error happens.
- Run with:  python -m pytest -q
"""
import pytest

from example import clamp


def test_value_inside_range_is_unchanged():
    # Given a value already inside the range
    # When we clamp it
    result = clamp(5, 0, 10)
    # Then it comes back unchanged
    assert result == 5


def test_value_below_range_becomes_low():
    assert clamp(-3, 0, 10) == 0


def test_value_above_range_becomes_high():
    assert clamp(42, 0, 10) == 10


def test_value_on_boundary_is_unchanged():
    assert clamp(10, 0, 10) == 10


def test_low_greater_than_high_raises():
    with pytest.raises(ValueError):
        clamp(5, 10, 0)
