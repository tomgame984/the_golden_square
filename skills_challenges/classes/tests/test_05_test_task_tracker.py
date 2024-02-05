import pytest
from lib.code_05_task_tracker import *

def test_empty_task_list():
    user_tasks = Task_Manager()
    assert user_tasks.open_tasks() == "No tasks outstanding."

def test_single_task_add_return_task_list():
    user_tasks = Task_Manager()
    user_tasks.add_task("Walk the dog")
    assert user_tasks.open_tasks() == ["Walk the dog"]

def test_duplicate_task_added_return_error_message():
    user_tasks = Task_Manager()
    user_tasks.add_task("Walk the dog")
    user_tasks.add_task("Walk the dog")
    assert user_tasks.open_tasks() == ["Walk the dog"]

def test_multiple_new_tasks_added_return_list():
    user_tasks = Task_Manager()
    user_tasks.add_task("Walk the dog")
    user_tasks.add_task("Cook dinner")
    user_tasks.add_task("Finish coding challenge")
    assert user_tasks.open_tasks() == ["Walk the dog", "Cook dinner", "Finish coding challenge"]

def test_multiple_new_tasks_with_multiple_duplicates_added_return_list():
    user_tasks = Task_Manager()
    user_tasks.add_task("Walk the dog")
    user_tasks.add_task("Cook dinner")
    user_tasks.add_task("Walk the dog")
    user_tasks.add_task("Finish coding challenge")
    user_tasks.add_task("Cook dinner")
    assert user_tasks.open_tasks() == ["Walk the dog", "Cook dinner", "Finish coding challenge"]

def test_delete_one_task_from_list_return_amended_list():
    user_tasks = Task_Manager()
    user_tasks.add_task("Walk the dog")
    user_tasks.add_task("Cook dinner")
    user_tasks.add_task("Finish coding challenge")
    user_tasks.complete_task("Walk the dog")
    assert user_tasks.open_tasks() == ["Cook dinner", "Finish coding challenge"]

def test_delete_only_item_from_list_return_message():
    user_tasks = Task_Manager()
    user_tasks.add_task("Cook dinner")
    user_tasks.complete_task("Cook dinner")
    assert user_tasks.open_tasks() == "No tasks outstanding."

def test_delete_multiple_tasks_from_list_return_amended_list():
    user_tasks = Task_Manager()
    user_tasks.add_task("Walk the dog")
    user_tasks.add_task("Cook dinner")
    user_tasks.add_task("Finish coding challenge")
    user_tasks.add_task("Watch TV")
    user_tasks.complete_task("Watch TV")
    user_tasks.complete_task("Cook dinner")
    assert user_tasks.open_tasks() == ["Walk the dog", "Finish coding challenge"]

def test_delete_one_task_that_does_not_exist_return_error_and_amended_list():
    user_tasks = Task_Manager()
    with pytest.raises(DoesNotExistException) as e:
        user_tasks.add_task("Cook dinner")
        user_tasks.add_task("Finish coding challenge")
        user_tasks.complete_task("Watch TV")
    assert str(e.value) == "Watch TV does not exist"
    assert user_tasks.open_tasks() == ["Cook dinner", "Finish coding challenge"]