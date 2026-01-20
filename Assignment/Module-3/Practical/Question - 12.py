#Write a Python program to demonstrate the use of local and global variables in a class.

#Global
a=45
b=68

print("Multiplication:",a*b)
class data:

    def mul(self):
     #Local
        a=22
        b=50
        print("Multiplication:",a*b)

dt = data()
dt.mul()



