from code_1_calculator import square

def test_square():
    try:
        assert square(2) == 4
        assert square(3) == 9
    except AssertionError:
        print("test case failed")

def main():
    test_square()


if __name__ == "__main__":
    main()