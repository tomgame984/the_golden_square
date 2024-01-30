from lib.counter import *

def test_counter_adds_five():
    counter = Counter()
    counter.add(5)
    result = counter.report()
    assert result == "Counted to 5 so far."

def test_counter_adds_one_hundred():
    counter = Counter()
    counter.add(100)
    result = counter.report()
    assert result == "Counted to 100 so far."

def test_counter_adds_five_six_hundred_forty_two():
    counter = Counter()
    counter.add(5642)
    result = counter.report()
    assert result == "Counted to 5642 so far."
