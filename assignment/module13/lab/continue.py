# This program skips 'banana'

List1 = ['apple', 'banana', 'mango']

for fruit in List1:
    if fruit == 'banana':
        continue   # Skip this iteration
    print(fruit)