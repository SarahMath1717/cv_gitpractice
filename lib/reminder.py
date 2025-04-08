# class Reminder:
#     def __init__(self, name):
#         self.name = name

#     def remind_me_to(self, task):
#         self.task = task

#     def remind(self):
#         return f"{self.task}, {self.name}!"
    # Initial answer, commented out for further expansion

class Reminder:
    def __init__(self, name):
        self.name = name
        self.task = None

    def remind_me_to(self, task):
        self.task = task

    def remind(self):
        # Look here! We want to fail if there is no reminder yet.
        if self.task is None:
            raise Exception("No reminder set!")
        return f"{self.task}, {self.name}!"