# {{Task Manager}} Class Design Recipe

## 1. Describe the Problem

* As a user:
    - So that I can keep track of my tasks, I want a program that I can:
        - Add todo tasks to.
        - See a list of them.
        
    - So that I can focus on tasks to complete, I want to:
        - Mark tasks as complete
        - Have completed tasks removed from the list.

## 2. Design the Class Interface

_Include the initializer, public properties, and public methods with all parameters, return values, and side-effects._

```python
# EXAMPLE

class Task_Manager:
    def __init__(self,):
        # Parameters:
        #   None
        # Side effects:
        #   creates a list for the user to add tasks.
        pass # No code here yet

    def add_task(self, task_details):
        # Parameters:
        #   task_details: string representing a single task 
        # Returns:
        #   Nothing
        # Side-effects
        #   Saves the task details to the self object
        pass # No code here yet

    def open_tasks(self):
        # Returns:
        #   A list of open tasks
        # Side-effects:
        #   Throws an exception if no task is set
        pass # No code here yet

    def complete_task(self, task_details):
        # Parameters:
        #   task_details: allow user to enter existing task details
        # Returns:
        #   Nothing
        # Side-effects
        #   Deletes task from self object.
        pass # No code here yet        
```

## 3. Create Examples as Tests

_Make a list of examples of how the class will behave in different situations._

``` python

def test_empty_task_list():
"""
Given no tasks added
Return a message "No tasks outstanding"
"""
users_tasks = Task_Manager()
user_tasks.open_tasks() # => "No tasks outstanding"

def test_single_task_add_return_task_list():
"""
Given a single new task is add
Return a list with the task
"""
users_tasks = Task_Manager()
user_tasks.add_task("Walk the dog")
user_tasks.open_tasks() # => ["Walk the dog"]

def test_duplicate_task_added_return_error_message():
"""
Given a single duplicate task is add
Return a message that the task already exists.
"""
users_tasks = Task_Manager()
user_tasks.add_task("Walk the dog")
user_tasks.add_task("Walk the dog")
user_tasks.open_tasks() # => "This task already exists"

def test_multiple_new_tasks_added_return_list():
"""
Given multi new tasks added
Return a list with the task
"""
users_tasks = Task_Manager()
user_tasks.add_task("Walk the dog")
user_tasks.add_task("Cook dinner")
user_tasks.add_task("Finish coding challenge")
user_tasks.open_tasks() # => ["Walk the dog", "Cook dinner", "Finish coding challenge"]

def test_multiple_new_tasks_with_multiple_duplicates_added_return_list():
"""
Give multiple new tasks added with multiple duplicates included
Return list without duplicate tasks included.
"""
user_tasks = Task_Manager()
user_tasks.add_task("Walk the dog")
user_tasks.add_task("Cook dinner")
user_tasks.add_task("Walk the dog")
user_tasks.add_task("Finish coding challenge")
user_tasks.add_task("Cook dinner")
user_tasks.open_tasks() => ["Walk the dog", "Cook dinner", "Finish coding challenge"]

def test_delete_one_task_from_list_return_amended_list():
"""
Given one item for the list is deleted
Return a list without out the deleted task included.
"""
users_tasks = Task_Manager()
user_tasks.add_task("Walk the dog")
user_tasks.add_task("Cook dinner")
user_tasks.complete_task("Walk the dog")
user_tasks.open_tasks() # => ["Cook dinner"]

def test_delete_only_item_from_list_return_message():
"""
Given the only item in the list is deleted
Return a message, "No outstanding tasks"
"""
users_tasks = Task_Manager()
user_tasks.add_task("Walk the dog")
user_tasks.complete_task("Walk the dog")
user_tasks.open_tasks() # => "No outstanding tasks"

def test_delete_multiple_tasks_from_list_return_amended_list():
"""
Given multi tasks are deleted
Return a list with the task
"""
users_tasks = Task_Manager()
user_tasks.add_task("Walk the dog")
user_tasks.add_task("Cook dinner")
user_tasks.add_task("Finish coding challenge")
user_tasks.add_task("Watch TV")
user_tasks.complete_task("Watch TV")
user_tasks.complete_task("Cook dinner")
user_tasks.open_tasks() # => ["Finish coding challenge"]

def test_delete_one_task_that_does_not_exist_return_error_and_amended_list():
"""
Given user tries to delete one item that isn't in list.
Return a message "This task does not exist" and return list of open task
"""
users_tasks = Task_Manager()
user_tasks.add_task("Walk the dog")
user_tasks.add_task("Cook dinner")
user_tasks.complete_task("Finish coding challenge")
user_tasks.open_tasks() # => "This task does not exist"  ["Walk the dog", "Cook dinner"]
```

_Encode each example as a test. You can add to the above list as you go._

## 4. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._
