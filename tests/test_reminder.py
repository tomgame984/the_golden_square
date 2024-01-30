from lib.reminder import *

def test_I_reminds_user_to_do_a_task():
    reminder = Reminder("Kay")
    reminder.remind_me_to("Walk the dog")
    assert reminder.remind() == "Walk the dog, Kay!"



