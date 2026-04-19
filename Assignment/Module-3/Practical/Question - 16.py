#Write a Python program to show hierarchical inheritance.

# Base class
class A:
    def base_class(self):
        print("This is Base Class")

# First Derived Class
class B(A):
    def first_derived(self):
        print("This is a First Derived Class")

# Second Derived Class
class C(A):
    def second_derived(self):
        print("This is a Second Derived Class")


obj1 = B()
obj2 = C()

obj1.base_class()
obj1.first_derived()
obj2.base_class()             
obj2.second_derived()  
