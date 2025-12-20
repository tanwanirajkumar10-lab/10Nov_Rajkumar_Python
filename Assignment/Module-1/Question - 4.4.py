# Write a Python program to check if a person is eligible to donate blood using a nested if.


age = int(input("Enter your Age: "))
has_illness = input("Do you have any illness? (Yes/No): ")

if age >= 25:
    if has_illness == "Yes" or has_illness == "yes":
        print("You are not eligible to donate blood.")
    else:
        print("You are eligible to donate blood.")
else:
    print("You are not eligible to donate blood because you are under 25 years old.")
