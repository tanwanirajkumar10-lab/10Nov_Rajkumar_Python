#Write a Python program to check the current position of the file cursor using tell()

file = open("hello.txt", "w")
file.write("Hello World")

position = file.tell()
print("Current Cursor Position:", position)

file.close()
