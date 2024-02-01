from lib.grammar_checker import *

def test_given_text_with_capital_and_full_stop():
    assert grammar_checker("Hello world.") == "Capital Letter: True\nEnd of sentence punctuation: True"