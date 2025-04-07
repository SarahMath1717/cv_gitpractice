from lib.check_codeword import *

def test__correct_check_codeword():
    result = check_codeword("horse")
    assert result == "Correct! Come in."

def test__close_check_codeword():
    result = check_codeword("hope")
    assert result == "Close, but nope."

def test__wrong_check_codeword():
    result = check_codeword("turtle")
    assert result == "WRONG!"