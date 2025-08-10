# creating a class

class Student:
    def __init__(self, name, matricule, gpa, gender):
        self.name = name
        self.matricule = matricule
        self.gpa = gpa
        self.gender = gender

    def register_course():
        pass



    def take_lesson(self):
        return f"{self.name} has matricule {self.matricule}"
    


# creating instances (objects) of the Student class
first_student = Student("Allen", "UBa23", 3.9, "male")
# second_student = Student("mbom", "UBa23655", 0.1, "other")
# print(f"First student name: {first_student.name}")
# print(f"First student matricule: {first_student.matricule}")
# print(f"First student gpa: {first_student.gpa}")
# print(f"First student gender: {first_student.gender}")

print(dir(first_student))
