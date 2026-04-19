#Write a Python program to show single inheritance.

class A:
    def a(self):
        print("Parent Class")

class B(A):
    def b(self):
        print("Child Class")

obj = B()
obj.a()
obj.b()