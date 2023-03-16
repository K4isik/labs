from functools import reduce
numbers = [1, 2, 3, 4, 5]
res = reduce(lambda x, y: x * y, numbers)
print("Product of all the numbers:", res)
