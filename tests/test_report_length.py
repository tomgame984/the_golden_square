from lib.report_length import *

def test_report_length_six_char():
    result = report_length("Thomas")
    assert result == "This string was 6 characters long."

def test_report_length_four_char():
    result = report_length("Lucy")
    assert result == "This string was 4 characters long."

def test_report_length_nine_char():
    result = report_length("Tottenham")
    assert result == "This string was 9 characters long."