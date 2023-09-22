class Student:
    def __init__(self, name, grades):
        self.name = name
        self.grades = grades
    
    def average_grade(self):
        return sum(self.grades) / len(self.grades)

student1 = Student("Bob", (100, 95, 93, 78, 90))
student2 = Student("Charlies", (70, 60, 65, 60, 80))

print(student1.name)
print(student1.grades)
print(student1.average_grade())

print(student2.name)
print(student2.grades)
print(Student.average_grade(student2))
