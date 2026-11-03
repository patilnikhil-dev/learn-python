from code_1_calculator import square

def test_square():
    assert square(2) == 4
    assert square(3) == 3
    assert square(-2) == 4
    assert square(-3) == 9
    assert square(0) == 0