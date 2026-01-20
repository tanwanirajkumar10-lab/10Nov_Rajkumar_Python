#Write a Python program to handle exceptions in a calculator.

try:
    a=int(input("Enter First Number:"))
    b=int(input("Enter Second Number:"))
    print("Sum:",a+b)
    print("Sub:",a-b)
    print("Mul:",a*b)
    print("Div:",a/b)

except Exception as e:
    print(e)