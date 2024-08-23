from fuel import convert
from fuel import gauge

def test_convert():
    assert convert("4/4") == 100
    assert convert("0/4") == 0.0
    assert convert("1/4") == 25.0

def test_guage():
    assert gauge(100) == "F"
    assert gauge(0.0) == "E"
    assert gauge(25.0) == "25.0%" 