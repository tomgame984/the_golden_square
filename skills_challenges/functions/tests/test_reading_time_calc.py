from lib.reading_time_calc import *

"""
Given a string with 200 words and no change to the WPM
Returns a statement of 'Based on 200 words per minute, this text will take 1 minutes to read.'
"""
def test_given_200_word_string_return_one_minute():
    result = reading_time_calculator(two_hundred_words) 
    assert result == 'This text will take about 1 minute(s) to read.'

"""
Given a string with 100 words and no change to the WPM
Returns a statement of 'Based on 200 words per minute, this text will less than a minute to read.'
"""
def test_given_100_word_string_return_less_than_one_minute():
    result = reading_time_calculator(one_hundred_words)
    assert result == 'This text will take less than a minute to read.'

"""
Given a string with 800 words and no change to the WPM.
Returns a statement of 'Based on 200 words per minute, this text will take 4 minutes to read.'
"""
def test_given_800_word_string_return_10_minutes():
    result = reading_time_calculator(two_thousand_words)
    assert result == 'This text will take about 4 minute(s) to read.'


"""
Given a empty string with n words and no change to the WPM.
Returns a statement of 'There is nothing to read!'
"""
def test_given_blank_string_return_no_words_message():
    result = reading_time_calculator("")
    assert result == 'There are no words to read!'