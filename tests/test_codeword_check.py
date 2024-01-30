from lib.check_codeword import *

def test_check_codeword_correct():
    result = check_codeword('horse')
    assert result == "Correct! Come in."

def test_check_codeword_first_last_indices_match():
    result = check_codeword("home")
    assert result == "Close, but nope."

def test_check_codeword_entirely_wrong():
    result = check_codeword("incorrect")
    assert result == "WRONG!"
