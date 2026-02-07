from stringcompression import compress_string

def test_basic():
    assert compress_string("aaabbc") == "a3b2c1"

def test_single():
    assert compress_string("a") == "a1"

def test_no_repeat():
    assert compress_string("abc") == "a1b1c1"

def test_empty():
    assert compress_string("") == ""
