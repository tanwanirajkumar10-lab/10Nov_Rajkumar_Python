#Write a Python program that uses a custom iterator to iterate over a list of integers.

class CustomIntIterator:
    
    def __init__(self, data):
        self.data = data
        self.index = 0

    def __iter__(self):
        
        return self

    def __next__(self):
        
        if self.index >= len(self.data):
            raise StopIteration
        value = self.data[self.index]
        self.index += 1
        return value

my_list = [10, 20, 30, 40, 50]
custom_iterator = CustomIntIterator(my_list)

print("Iterating over the list using the custom iterator:")
for number in custom_iterator:
    print(number)
