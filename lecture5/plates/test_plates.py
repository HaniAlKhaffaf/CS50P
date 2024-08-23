from plates import is_valid


def test_start_atleast_two_letter():
    assert is_valid("CS50") == True
    assert is_valid("C50") == False

def test_max_min_char():
    assert is_valid("CSP50") == True
    assert is_valid("CSP5000") == False

def test_number_middle():
    assert is_valid("CS50P") == False

def test_period_space_punct():
    assert is_valid("CS50!") == False
    assert is_valid(" CS50") == False