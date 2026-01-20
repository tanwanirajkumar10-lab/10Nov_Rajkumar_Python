#Write a Python program to demonstrate the use of super() in inheritance.

class Company:
    def __init__(self, name):
        self.name = name 

    def show_name(self):
        print("Name:", self.name)

class Employee(Company):
    def __init__(self, name, grade):
        super().__init__(name)  
        self.grade = grade      

    def show_grade(self):
        print("Grade:", self.grade)

obj = Employee("Rajkumar", "A")

obj.show_name()   
obj.show_grade() 
