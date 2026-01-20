#Write a Python program to demonstrate handling multiple exceptions.

try:
    num1=int(input("Enter First Number:"))
    num2=int(input("Enter Second Number:"))

    print("Division is:",num1/num2)

except ZeroDivisionError:
    print("Cannot divide by zero")

except ValueError:
    print("Error: Invalid input")

except Exception as e:
    print(e)