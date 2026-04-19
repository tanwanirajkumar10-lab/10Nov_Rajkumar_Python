#Write a Python program to handle file exceptions and use the finally block for closing the file.

try:
    file = open("file.txt", "r")
    lines = file.read()
    print(lines)

except FileNotFoundError:
    print("Error: File not found!")

except Exception as e:
    print("An unexpected error occurred:",e)

finally:
    file.close()
