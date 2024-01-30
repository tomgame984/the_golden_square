from lib.add_five import *

def test_initial_state_returns_five():
    assert add_five(0) == 5

def test_add_five_returns_eight_for_three():
    assert add_five(3) == 8

def test_add_neg_three_returns_two():
    assert add_five(-3) == 2
    