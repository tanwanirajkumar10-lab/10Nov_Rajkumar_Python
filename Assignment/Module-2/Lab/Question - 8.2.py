#Write a Python program to create a calculator using functions.

num1=int(input("Enter First Number:"))
num2=int(input("Enter Second Number:"))

def add(a,b):
    print("Addition is:",a+b)

def sub(a,b):
    print("Subtraction is:",a-b)
    
def mul(a,b):
    print("Multiplication is:",a*b)
    
def div(a,b):
    print("Division is:",a/b)
    

print("Select your choice:")

print("1:Addition")
print("2:Subtraction")
print("3:Multiplication")
print("4:Division")

choice=int(input("Select any one option:"))

if choice==1:
    add(num1,num2)
elif choice==2:
    sub(num1,num2)
elif choice==3:
    mul(num1,num2)
elif choice==4:
    div(num1,num2)
else:
    print("Error!Invalid choice...")
