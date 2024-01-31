from lib.make_snippet import *

# A function called make_snippet that takes a string as an argument
# and returns the first five words and then a '...' if there are more than that.

"""
Given a string <= 5 words.
Return the string
"""

def test_given_str_0_words_return_str():
    result = make_snippet('')
    assert result == ''

def test_given_str_4_words_return_str():
    result = make_snippet('My name is Tom')
    assert result == 'My name is Tom'

def test_given_str_5_words_return_str():
    result = make_snippet('Hello, my name is Tom')
    assert result == 'Hello, my name is Tom'

"""
Given a string longer than 5 words
Return first 5 words and suffix with '...'
"""

def test_given_str_6_words_return_first_5_words_and_3_dots():
    result = make_snippet('Hello, my name is Tom Game.')
    assert result == 'Hello, my name is Tom...'

def test_given_str_more_than_6_words_return_first_5_words_and_3_dots():
    result = make_snippet('Hello, my name is Tom Game. I am an Apprentice.')
    assert result == 'Hello, my name is Tom...'