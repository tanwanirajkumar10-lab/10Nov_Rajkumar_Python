#Write a generator function that generates the first 10 even numbers.

def Even_Num():
    num = 2
    count = 0
    while count < 10:
        yield num
        num += 2
        count += 1

# Create generator object
even_gen = Even_Num()

# Print the first 10 even numbers
for even in even_gen:
    print(even)
