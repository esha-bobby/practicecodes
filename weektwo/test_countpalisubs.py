from countpalisubs import count_palindromes

def test_basic():
    assert count_palindromes("aaa") == 6

def test_normal():
    assert count_palindromes("abbabba") == 13

def test_empty():
    assert count_palindromes("") == 0
