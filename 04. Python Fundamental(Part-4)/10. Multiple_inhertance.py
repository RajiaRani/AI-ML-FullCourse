# Two differnet classes ki property use karte hai
# stydent class -> teacher class -> teaching assistant class

class Teacher:
    def __init__(self, salary):
        self.salary = salary

class Student:
    def __init__(self, gpa):
        self.gpa = gpa

class TA(Teacher, Student):
    def __init__(self, salary, gpa, name):
        Teacher.__init__(self, salary)
        Student.__init__(self, gpa)
        self.name = name


TA1 = TA( 1200000, 9.9, "Rajia Rani")
print(TA1.name, TA1.salary, TA1.gpa)
        