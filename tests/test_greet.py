from lib.greet import *

def test_greet_hello():
    result = greet("Sophia")
    assert result == f"Hello, Sophia!"