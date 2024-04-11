class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def display_info(self):
        print("Name:", self.name)
        print("Age:", self.age)

class Student(Person):
    def __init__(self, name, age, roll_number):
        super().__init__(name, age)
        self.roll_number = roll_number
    
    def display_info(self):
        super().display_info()
        print("Roll Number:", self.roll_number)

student = Student("Alice", 20, "S001")
student.display_info()