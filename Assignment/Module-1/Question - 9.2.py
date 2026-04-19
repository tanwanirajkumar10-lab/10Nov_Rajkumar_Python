#Write a Python program that manipulates and prints strings using various string methods.

str = "Hello Hi"
str1 = " HelloHi "
str2 = "Hello123"

print("capitalize:",str.capitalize())
print("title:",str.title())
print("casefold:",str.casefold())
print("center:",str.center(50,'*'))
print("count:",str.count('H'))
print("endswith:",str.endswith('i'))
print("find:",str.find('Hi'))
print("index:",str.index('Hello'))
print("lower:",str.lower())
print("upper:",str.upper())

print("strip:",str1.strip())
print("lstrip:",str1.lstrip())
print("rstrip:",str1.rstrip())
print("replace:",str.replace('Hello','Hi'))

print("isalnum():", str2.isalnum())
print("isalpha():", str2.isalpha())
print("isdigit():", str2.isdigit())
print("isdecimal():", str2.isdecimal())
print("isnumeric():", str2.isnumeric())
print("isascii():", str2.isascii())
print("islower():", str2.islower())
print("isupper():", str2.isupper())
print("istitle():", str2.istitle())
print("isspace():", str2.isspace())