from lib.grammar_checker import *

def test_given_text_with_capital_and_full_stop():
    assert grammar_checker("Hello world.") == "Capital Letter: True\nEnd of sentence punctuation: True"

def test_given_text_with_capital_but_no_full_stop():
    assert grammar_checker("Hello world") == "Capital Letter: True\nEnd of sentence punctuation: False"

def test_given_lowercase_first_letter_and_full_stop():
    assert grammar_checker("hello world.") == "Capital Letter: False\nEnd of sentence punctuation: True"

def test_given_lowercase_first_letter_and_no_full_stop():
    assert grammar_checker("hello world") == "Capital Letter: False\nEnd of sentence punctuation: False"

def test_given_text_with_capital_and_with_accepted_punctuation():
    assert grammar_checker("Hello world!") == "Capital Letter: True\nEnd of sentence punctuation: True"

def test_given_text_without_capital_and_incorrect_punctuation():
    assert grammar_checker("hello world;") == "Capital Letter: False\nEnd of sentence punctuation: False"

