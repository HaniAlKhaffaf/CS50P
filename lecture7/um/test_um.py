from um import count

def test_seperate_um():
    assert count("um") == 1
    assert count("Hello, um , world") == 1

def test_um_with_words():
    assert count("yummy") == 0
    assert count("yum yum um") == 1
    assert count("Hello, um, world") == 1

def test_multiple_um():
    assert count("Hello, um, world, um") == 2
    assert count("um um um um") == 4 
    assert count("hello um um um um hello um") == 5