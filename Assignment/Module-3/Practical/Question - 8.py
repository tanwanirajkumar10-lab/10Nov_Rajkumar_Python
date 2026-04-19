#Write a Python program to handle multiple exceptions (e.g., file not found, division by zero).

try:
    file = open("file.txt", "r")
    lines = file.read()
    print(lines)

    num1 = int(input("Enter First Number:"))
    num2 = int(input("Enter Second Number:"))
    print("Division is:",num1/num2)

except FileNotFoundError:
    print("Error: File not found!")

except ZeroDivisionError:
    print("Error: Cannot divide by zero!")

except ValueError:
    print("Error: Invalid input! Please enter valid numbers.")

except Exception as e:
    print("An unexpected error occurred:",e)
