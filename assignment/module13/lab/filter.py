# Using filter to get even numbers

nums = [1, 2, 3, 4, 5, 6]

even_nums = list(filter(lambda x: x % 2 == 0, nums))
print(even_nums)