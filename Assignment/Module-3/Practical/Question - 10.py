#Write a Python program to print custom exceptions.

class NegativeValueError(Exception):
    pass

def check_value(val):
    if val < 0:
        raise NegativeValueError("Negative values are not allowed!")

try:
    num = int(input("Enter a positive number:"))
    check_value(num)
    print("Number is:", num)

except NegativeValueError as e:
    print(e)

except ValueError:
    print("Invalid input! Please enter an integer.")
