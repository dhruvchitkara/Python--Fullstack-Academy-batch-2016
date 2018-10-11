class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def display(self):
        print('This is the Person Class')
        print(f'Name : {self.name}')
        print(f'Age : {self.age}')

class Teacher(Person):
    def __init__(self,name,age,experience,research):
        Person.__init__(self,name,age)
        self.experience = experience
        self.research = research

    def display(self):
        print(f'This is the Teacher Class')
        Person.display(self)
        print(f'Experience : {self.experience}')
        print(f'Research : {self.research}')

class Student(Person):
    def __init__(self,name,age,courses,marks):
        Person.__init__(self,name,age)
        self.courses = courses
        self.marks = marks

    def display(self):
        print(f'This is the Student Class')
        Person.display(self)
        print(f'Courses : {self.courses}')
        print(f'Marks : {self.marks}')

teacher_obj = Teacher('Naman','21','5 Years','Kuch nii')
teacher_obj.display()

student_obj = Student('Naman','21','BE','8.0')
student_obj.display()























































































