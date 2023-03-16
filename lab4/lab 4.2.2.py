n = int(input())
generator = (i for i in range(1, n + 1))
for num in generator:
    if num % 2 == 0:
        print(num, end=", ")
