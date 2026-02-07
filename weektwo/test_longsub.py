from longsub import longest_unique_substring

def test_basic():
    assert longest_unique_substring("abcabcbb") == 3

def test_all_unique():
    assert longest_unique_substring("abcd") == 4

def test_same():
    assert longest_unique_substring("aaaa") == 1

def test_empty():
    assert longest_unique_substring("") == 0
