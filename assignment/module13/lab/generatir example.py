# Generator to produce even numbers

def even_numbers():
    for i in range(2, 21, 2):
        yield i   # Returns value one by one

for num in even_numbers():
    print(num)