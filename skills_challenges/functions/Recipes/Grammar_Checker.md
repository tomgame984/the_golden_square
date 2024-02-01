# {{Grammar Checker}} Function Design Recipe

## 1. Describe the Problem

As a user
So that I can improve my grammar
I want to verify that a text starts with a capital letter and ends with a suitable sentence-ending punctuation mark.

## 2. Design the Function Signature

_Include the name of the function, its parameters, return value, and side effects._

```python

def grammar_checker(text):
    """Checks that a sentence has:
            1. A capital letter.
            2. The end of the sentence has ". ! ? :"
    
    Parameters: (list all parameters and their types)
        text : a string containing words (e.g. "Hello world.")

    Returns: (state the return value and its type)
        Boolean values within a string.
        'Capital Letter: True/False'
        'End of sentence punctuation:  True/False'

    Side effects: (state any side effects)
        This function doesn't print anything or have any other side-effects
    """
    pass # Test-driving means _not_ writing any code here yet.
```

## 3. Create Examples as Tests

_Make a list of examples of what the function will take and return._

```python
# EXAMPLE

def test_given_text_with_capital_and_full_stop():
"""
Given a text string starting with a capital letter and ending with a full stop
It returns:
    'Capital Letter: True'
    'End of sentence punctuation:  True'
"""
grammar_check("Hello world.") => 
    'Capital Letter: True'
    'End of sentence punctuation:  True'

def test_given_text_with_capital_but_no_full_stop():
"""
Given a text string starting with a capital letter and missing a full stop
It returns:
    'Capital Letter: True'
    'End of sentence punctuation:  False'
"""
grammar_check("Hello world") => 
    'Capital Letter: True'
    'End of sentence punctuation:  False'

def test_given_lowercase_first_letter_and_full_stop():
"""
Given a text string starting with lowercase letter and ending with a full stop
It returns:
    'Capital Letter: False'
    'End of sentence punctuation:  True'
"""
grammar_check("hello world.") => 
    'Capital Letter: False'
    'End of sentence punctuation:  True'

def test_given_lowercase_first_letter_and_no_full_stop():
"""
Given a text string starting with lowercase letter and ending without any punctuation.
It returns:
    'Capital Letter: False'
    'End of sentence punctuation:  False'
"""
grammar_check("hello world") => 
    'Capital Letter: False'
    'End of sentence punctuation:  False'

def test_given_text_with_capital_and_with_accepted_punctuation():
"""
Given a text string starting with a capital letter and ending with acceptable punctuation.
It returns:
    'Capital Letter: True'
    'End of sentence punctuation:  True'
"""
grammar_check("Hello world!") => 
    'Capital Letter: True'
    'End of sentence punctuation:  True'

def test_given_text_without_capital_and_incorrect_punctuation():
"""
Given a text string starting without a capital letter and ending incorrect punctuation.
It returns:
    'Capital Letter: True'
    'End of sentence punctuation:  False'
"""
grammar_check("hello world;") => 
    'Capital Letter: False'
    'End of sentence punctuation:  False'
```

_Encode each example as a test. You can add to the above list as you go._

## 4. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._

Here's an example for you to start with:

```python
# EXAMPLE

from lib.extract_uppercase import *

"""
Given a lower and an uppercase word
It returns a list with the uppercase word
"""
def test_extract_uppercase_with_upper_then_lower():
    result = extract_uppercase("hello WORLD")
    assert result == ["WORLD"]
```

Ensure all test function names are unique, otherwise pytest will ignore them!
