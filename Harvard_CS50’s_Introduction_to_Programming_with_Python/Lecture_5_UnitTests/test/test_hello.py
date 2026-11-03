from code_5_hello import hello

def test_default():
    assert hello() == "hello, world"

def test_arguments():
    for name in ["Nikhil", "Rahul", "Akshay"]:
        assert hello(name) == f"hello, {name}"