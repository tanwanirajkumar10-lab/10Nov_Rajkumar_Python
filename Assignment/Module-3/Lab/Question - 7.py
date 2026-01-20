#Write Python programs to demonstrate different types of inheritance (single, multiple, multilevel, etc.).

#Single Inheritance

class A:
    def a(self):
        print("Parent Class")

class B(A):
    def b(self):
        print("Child Class")

obj = B()
obj.a()
obj.b()

#---------------------------------------
#Multiple Inheritance

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

#---------------------------------------
#Multilevel Inheritance

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
