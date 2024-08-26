from numb3ers import validate


#going to be the function for testing the number value
def test_number_validate():
    assert validate("0.0.0.0") == True
    assert validate("255.255.255.255") == True
    assert validate("255.275.255.255") == False
    assert validate("0.0.-1.0") == False


def test_period_validate():
    assert validate("0.0.0.0.") == False
    assert validate(".0.0.0.0") == False
    assert validate("255,255,255,255") == False
    assert validate("255.255.255") == False