class Task_Manager():
    def __init__(self):
        self.tasks = []
        self._duplicates = []
    
    def add_task(self, task_details):
        if task_details not in self.tasks:
            self.tasks.append(task_details)

    def open_tasks(self):
        if len(self.tasks) == 0:
            return "No tasks outstanding."
        return self.tasks
    
    def complete_task(self, task_details):
        if task_details in self.tasks:
            self.tasks.remove(task_details)
        else:
            raise DoesNotExistException(f"{task_details} does not exist")
        
class DoesNotExistException(Exception):
    pass

    

