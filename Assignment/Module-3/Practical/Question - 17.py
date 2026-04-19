#Write a Python program to show hybrid inheritance.


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

class D(B,C):
    def third_derived(self):
        print("This is a Third Derived Class")


obj = D()

obj.base_class()
obj.first_derived()
obj.second_derived()  
obj.third_derived()  