#Write a Python program to write multiple strings into a file.

file=open("new.txt","w")
lines=["Hello\n","World\n","Hi\n"]
file.writelines(lines)
file.close()