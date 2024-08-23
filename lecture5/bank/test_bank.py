from bank import value

def test_hello_greeting():
    assert value("hello") == 0
    assert value("Hello") == 0

def test_h_greeting():
    assert value("hey") == 20
    assert value("Hey") == 20

def test_any_greeting():
    assert value("what's up") == 100
    assert value("What's up") == 100