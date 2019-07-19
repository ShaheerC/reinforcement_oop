class Task:

    def __init__(self):
        pass

    def description(self, describe_task):
        self.describe_task = describe_task
        return "The task is {}".format (self.describe_task)

    def due_date(self, date):
        self.date = date
        return "The due date is {}".format(self.date)