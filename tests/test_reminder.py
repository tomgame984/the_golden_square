import pytest
from lib.reminder import *

def test_I_reminds_user_to_do_a_task():
    reminder = Reminder('Kay')
    reminder.remind_me_to("Walk the dog")
    assert reminder.remind() == "Walk the dog, Kay!"

def test_reminder():
    reminder = Reminder('Kay')
    with pytest.raises(NoReminderSetException) as e:
        reminder.remind()
    error_message = str(e.value)
    assert error_message == "No reminder set!"


