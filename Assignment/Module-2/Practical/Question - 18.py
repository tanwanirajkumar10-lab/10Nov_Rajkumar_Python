#Write a Python program to count how many times each character appears in a string.

str1 = "Hello Hi How are you"
char_count = {}

for i in str1:
        if i in char_count:
            char_count[i] += 1
        else:
            char_count[i] = 1

print(char_count)