def squares_gen(a, b):
    for i in range(a, b+1):
        yield i ** 2

a = int(input())
b = int(input())

squares = squares_gen(a, b)

for i in squares:
    print(i, end=", ")
