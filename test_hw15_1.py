import pytest

from hw15_1 import convert_miles_to_km


def test_convert_miles_to_km():
    miles = 1
    expected_km = 1.6
    assert convert_miles_to_km(miles=miles) == expected_km


def test_convert_miles_to_km_v2():
    miles = 2
    expected_km = 3.2
    assert convert_miles_to_km(miles=miles) == expected_km


def test_convert_miles_to_km_negative():
    miles = -2
    with pytest.raises(ValueError):
        assert convert_miles_to_km(miles=miles)
