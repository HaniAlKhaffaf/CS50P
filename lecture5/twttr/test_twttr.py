from twttr import shorten


def test_word():
    assert shorten("Hello") == "Hll"


def test_sentence():
    assert shorten("Welcome to CS50") == "Wlcm t CS50"
