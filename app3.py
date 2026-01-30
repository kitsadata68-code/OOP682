from models.classroom import ClassRoom
from models.student import Student


oop = ClassRoom("OOP")
oop.add_student(Student(1, "Alice", 20,"s001"))
oop.add_student(Student(2, "Bob", 22,"s002"))
print(f'OOP registered students in {len(oop)} students.')
oop.add_student(Student(3, "Charlie", 21,"s003"))
print(len(oop))
print('students in the class:')
for i in range(len(oop)):
    print(oop[i])