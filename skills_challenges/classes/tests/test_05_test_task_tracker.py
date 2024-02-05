from lib.code_05_task_tracker import *

def test_empty_task_list():
    user_tasks = Task_Manager()
    assert user_tasks.open_tasks() == "No tasks outstanding."