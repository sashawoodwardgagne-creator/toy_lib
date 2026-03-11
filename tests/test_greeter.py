from toy_lib import greet

def test_greet():
    assert greet("Sasha").startswith("Hello, Sasha")
