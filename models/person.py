from models.person import Person


class Person:
    def __init__(self,pid , name, age,):
        self.pid = pid
        self.name = name
        self.age = age

    def __str__(self):
        return f"person[PID: {self.pid}, Name: {self.name}, Age: {self.age}]"