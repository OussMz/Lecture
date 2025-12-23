class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        return f"Hello, my name is {self.name} and I am {self.age} years old."
    
class Student(Person):
    def __init__(self, name, age,student_id):
        super().__init__(name, age)
        self.student_id = student_id
    def introduce(self):
        parent_intro = super().introduce()
        return f"{parent_intro} My student ID is {self.student_id}."
class Teacher(Person):
    def __init__(self, name, age, subject):
        super().__init__(name, age)
        self.subject = subject
    def introduce(self):
        parent_intro = super().introduce()
        return f"{parent_intro} I teach {self.subject}."
# Example usage:
student = Student("Alice", 20, "S12345")                
teacher = Teacher("Mr. Smith", 40, "Mathematics")
print(student.introduce())  # Output: Hello, my name is Alice and I am 20 years old. My student ID is S12345.
print(teacher.introduce())  # Output: Hello, my name is Mr. Smith and I am 40 years old. I teach Mathematics.


