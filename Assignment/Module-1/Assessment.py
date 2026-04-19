#Create a mini-project where students combine conditional statements, loops, and functions to create a basic Python application, such as a simple calculator or a grade management system.

subjects = int(input("How many subject's mark you want to calculate ?:"))
data={}

for i in range(subjects):

    subject_name = input(f"Enter Name of Subject {i+1}: ")
    marks = float(input(f"Enter Marks for {subject_name}: "))
    data[subject_name] = marks
    
print("Result".center(50,'-'))
total = sum(data.values())
print("Total Marks:",total)
percentage = total/subjects
print("Percentage:", percentage)


def get_grade():

    if percentage>=90:
        return"A Grade"
    elif percentage>=80:
        return"B Grade"
    elif percentage>=70:
        return"C Grade"
    elif percentage>=60:
        return"D Grade"
    elif percentage>=50:
        return"E Grade"
    else:
        return"Fail"

x = get_grade()
print("Grade:",x)
