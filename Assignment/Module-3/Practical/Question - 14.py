#Write a Python program to show multilevel inheritance.

class A:
    def a(self):
        print("Grandfather Class")

class B(A):
    def b(self):
        print("Father Class")
    
class C(B):
    def c(self):
        print("Son Class")

obj = C()
obj.a()
obj.b()
obj.c()