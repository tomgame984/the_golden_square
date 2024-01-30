from lib.greet import *

def test_greet_returns_hello_and_name():
    result = greet('Tom')
    assert result == 'Hello, Tom!'