from lib.check_codeword import *

def test_check_codeword_correct():
    assert check_codeword('horse') == "Correct! Come in."

def test_check_codeword_first_last_indices_match():
    assert check_codeword("home") == "Close, but nope."

def test_check_codeword_first_indices_only_match():
    assert check_codeword("hot") == "WRONG!"

def test_check_codeword_entirely_wrong():
    assert check_codeword("incorrect") == "WRONG!"
