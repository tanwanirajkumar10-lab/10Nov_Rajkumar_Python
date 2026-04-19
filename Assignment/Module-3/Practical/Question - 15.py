#Write a Python program to show multiple inheritance.

class A:
    def a(self):
        print("Grandfather Class")

class B:
    def b(self):
        print("Father Class")
    
class C(A,B):
    def c(self):
        print("Son Class")

obj = C()
obj.a()
obj.b()
obj.c()
