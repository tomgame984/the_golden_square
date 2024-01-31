from lib.count_words import *

# *** Design ***
# A function called count_words
# Takes a string as an argument
# Returns the number of words in that string.

"""
Test:
Given a string of just words
Returns the number of words in the string
"""

def test_given_str_with_only_3_words_returns_word_count_as_3():
    result = count_words("String lengths change")
    assert result == 3

"""
Test:
Given a string consisting of just numbers
returns 0 as number of words in the string
"""

def test_given_str_just_numbers_returns_word_count_as_zero():
    result = count_words("1 2 3 4 5")
    assert result == 0

"""
Test:
Given a string consisting of 4 words and 1 number
Return the count of the words only.
"""

def test_given_str_with_one_int_included_return_word_count():
    result = count_words("This sentence has 1 number")
    assert result == 4

"""
Test:
Given a string consisting of 4 words and 1 number >9
Return the count of the words only.
"""

def test_given_str_with_int_great_than_9_included_return_word_count():
    result = count_words("This sentence includes 4758 in it.")
    assert result == 5

