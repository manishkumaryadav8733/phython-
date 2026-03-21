# This program checks whether a number is prime

num = int(input("Enter number: "))
is_prime = True   # Assume number is prime

if num <= 1:
    is_prime = False   # Numbers <= 1 are not prime
else:
    for i in range(2, num):
        if num % i == 0:
            is_prime = False   # Divisible means not prime

if is_prime:
    print("Prime number")
else:
    print("Not a prime number")