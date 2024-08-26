from working import convert
import pytest

def test_hour_convert():
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"
    assert convert("5 PM to 9 AM") == "17:00 to 09:00"
    assert convert("8 AM to 4 PM") == "08:00 to 16:00"

def test_hour_min_convert():
    assert convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"
    assert convert("9:30 AM to 5:30 PM") == "09:30 to 17:30"
    assert convert("5:00 PM to 9:00 AM") == "17:00 to 09:00"

def test_format_convert():

    assert convert("9 AM to 5:00 PM") == "09:00 to 17:00"

    with pytest.raises(ValueError):
        convert("9 AM - 5 PM")

    with pytest.raises(ValueError):
        convert("9 AM : 5 PM")

    with pytest.raises(ValueError):
        convert("Nine AM to five PM")
