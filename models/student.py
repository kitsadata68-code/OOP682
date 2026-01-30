from models.person import Student

class Student:
    def __init__(self,pid , name, age,):
        self.pid = pid
        self.name = name
        self.age = age

    def __str__(self):
        return f"Student[{self.pid}, Name: {self.name}, Age: {self.age}]"