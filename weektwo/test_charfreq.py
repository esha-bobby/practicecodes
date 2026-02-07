from charfreq import char_frequency

def test_basic():
    assert char_frequency("hello") == {
        "h":1, "e":1, "l":2, "o":1
    }

def test_empty():
    assert char_frequency("") == {}

def test_same_chars():
    assert char_frequency("aaa") == {"a":3}
