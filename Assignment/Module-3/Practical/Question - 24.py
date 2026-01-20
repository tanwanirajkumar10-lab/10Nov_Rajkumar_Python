#Write a Python program to match a word in a string using re.match().

import re

mystr="Hello World,Python is easy to learn"

x=re.match("Python",mystr)

if x:
    print("Match done!")
else:
    print("Not Found!")