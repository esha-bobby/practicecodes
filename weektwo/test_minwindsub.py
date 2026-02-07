from minwindsub import min_window

def test_basic():
    assert min_window("ADOBECODEBANC", "ABC") == "BANC"

def test_exact():
    assert min_window("abc", "abc") == "abc"

def test_not_found():
    assert min_window("abc", "z") == ""

def test_empty_t():
    assert min_window("abc", "") == ""
