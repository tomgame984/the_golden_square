import pytest
from lib.present import *

def test_wrap_and_unwrap():
    present = Present()
    present.wrap("xbox")
    assert present.unwrap() == "xbox"

def test_already_wrapped():
    present = Present()
    present.wrap('xbox')
    with pytest.raises(AlreadyWrappedException) as e:
        present.wrap('playstation')
    error_message = str(e.value)
    expected_msg = "A contents has already been wrapped."
    assert error_message == expected_msg

def test_unwrap_without_wrapping():
    present = Present()
    with pytest.raises(NoContentsWrappedException) as e:
        present.unwrap()
    error_message = str(e.value)
    assert error_message == "No contents have been wrapped."

def test_already_wrapped():
    present = Present()
    present.wrap('xbox')
    with pytest.raises(AlreadyWrappedException) as e:
        present.wrap('playstation')
    message = str(e.value)
    assert message == "A contents has already been wrapped."
        
    