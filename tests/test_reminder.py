from lib.reminder import *

def test_reminds_the_user_to_do_a_task():
    reminder = Reminder("Kay")
    reminder.remind_me_to("Walk the dog")
    result = reminder.remind()
    assert result == "Walk the dog, Kay!"

# import pytest # <-- New code
# from lib.reminder import *


# def test_reminder():
#     reminder = Reminder("Kay")
#     with pytest.raises(Exception) as e: # <-- New code
#         reminder.remind()
#     error_message = str(e.value) # <-- New code
#     assert error_message == "No reminder set!"