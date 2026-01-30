class Person:
    def __init__(self, pid, name, age):
        self.pid = pid
        self.name = name
        self.age = age
    
class Student(Person):
    def __init__(self,pid , name, age, studen_id):
        super().__init__(pid, name, age)
        self.age = age
        self.student_id = studen_id
        def __str__(self):
            return f"Student_id: {self.student_id}, Name: {self.name}, Age: {self.age}"
        
class staff(Person):
    def __init__(self, pid, name, age, staff_id):
        super().__init__(pid, name, age)
        self.staff_id = staff_id
    def __str__(self):
        return f"Staff_id: {self.staff_id}, Name: {self.name}, Age: {self.age}"

student1 = Student(1234567890123, "Alice", 20, "S1001")
staff1 = staff(1234567890123, "Bob", 35, "ST2001")
print(f"Student: {student1.name}, Age: {student1.age}, Student ID: {student1.student_id}")
print(f"Staff: {staff1.name}, Age: {staff1.age}, Staff ID: {staff1.staff_id}")

def get_person_info(person):
    print(isinstance(person, Person))
    return f"Name: {person.name}, Age: {person.age}"

get_person_info(student1) #returns "Name: Alice, Age: 20"
get_person_info(staff1) #returns "Name: Bob, Age: 35"

class Employee:
    pass

manager = Employee()
get_person_info(manager) # raises an error
