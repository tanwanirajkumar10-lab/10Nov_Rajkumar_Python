#Write a Python program to search for a word in a string using re.search()

import re

mystr="Hello World, Python is easy to learn"

x=re.search("Python",mystr)
print(x)

if x:
    print("Match done!")
else:
    print("Not Found!")