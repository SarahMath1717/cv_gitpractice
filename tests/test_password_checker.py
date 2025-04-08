import pytest
from lib.password_checker import *

def test_short_password():
    password = PasswordChecker()
    with pytest.raises(Exception) as not_long_enough:
        password.check("car")
    assert str(not_long_enough.value) == "Invalid password, must by 8+ characters."

def test_long_password():
    password = PasswordChecker()
    result = password.check("redlorryyellowlorry")
    assert result is True
