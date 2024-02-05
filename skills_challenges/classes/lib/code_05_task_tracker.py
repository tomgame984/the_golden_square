class Task_Manager():
    def __init__(self):
        self.tasks = []
    
    def add_task(self, task_details):
        self.tasks.append(task_details)
        print("** Task added **")
        return

    def open_tasks(self):
        if len(self.tasks) == 0:
            return "No tasks outstanding."
        return self.tasks
    
