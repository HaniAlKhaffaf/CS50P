from jar import Jar
import pytest

def test_init():
    jar1 = Jar()
    assert jar1.capacity == 12
    assert jar1.size == 0

    jar2 = Jar(10)
    assert jar2.capacity == 10
    assert jar2.size == 0

def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"


def test_deposit():
    jar = Jar(10)

    jar.deposit(5)
    assert jar.size == 5

    jar.deposit(5)
    assert jar.size == 10

    with pytest.raises(ValueError):
        jar.deposit(1)


def test_withdraw():
    jar = Jar(10)

    jar.deposit(8)
    jar.withdraw(3)
    assert jar.size == 5

    jar.withdraw(5)
    assert jar.size == 0

    with pytest.raises(ValueError):
        jar.withdraw(1)