class Task:

    def __init__(self, description, due_date):
        self.description = description
        self.due_date = due_date

class TodoList:

    def __init__(self):
        self.task_list = []

    def add_task (self, taskvar):
        self.task_list.append(taskvar)


laundry = Task('Clean your clothes', 'July 21')
vacuum = Task('Clean your floors', 'July 21')
groceries = Task('Buy food', 'July 20')

julylist = TodoList()

julylist.add_task(laundry)
julylist.add_task(vacuum)
julylist.add_task(groceries)