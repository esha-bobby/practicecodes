from capitalise import cap_first_last

def test_normal():
    assert cap_first_last("hello world") == "HellO WorlD"

def test_single_letter():
    assert cap_first_last("a b") == "A B"

def test_empty():
    assert cap_first_last("") == ""
