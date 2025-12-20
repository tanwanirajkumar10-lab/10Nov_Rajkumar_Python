#Write a Python program to calculate grades based on percentage using if-else ladder.

pr = float(input("Enter your Percentage: "))

if pr>=90:
    print("A Grade")
elif pr>=70:
    print("B Grade")
elif pr>=50:
    print("C Grade")
else:
    print("Fail")