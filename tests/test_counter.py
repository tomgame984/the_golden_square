from lib.counter import *

def test_counter_initial_state():
    counter = Counter()
    assert counter.report() == "Counted to 0 so far."

def test_counter_adds_five():
    counter = Counter()
    counter.add(5)
    assert counter.report() == "Counted to 5 so far."

def test_counter_adds_multiple_nums_to_count():
    counter = Counter()
    counter.add(5)
    counter.add(10)
    assert counter.report() == "Counted to 15 so far."

def test_counter_adds_minus_num():
    counter = Counter()
    counter.add(-8)
    assert counter.report() == "Counted to -8 so far."

def test_counter_add_multiple_minus_nums():
    count = Counter()
    count.add(-8)
    count.add(-12)
    assert count.report() == "Counted to -20 so far."

def test_counter_adds_pos_and_neg_nums():
    count = Counter()
    count.add(-8)
    count.add(12)
    assert count.report() == "Counted to 4 so far."