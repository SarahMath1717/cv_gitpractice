from lib.report_length import *

def test_report_length_long():
    result = report_length("antidisestablishmentarianism")
    assert result == "This string was 28 characters long."

def test_report_length_short():
    result = report_length("cake")
    assert result == "This string was 4 characters long."