def down_to_zero(n):
    for i in range(n, 0, -1):
        yield i

n = int(input())
gen = down_to_zero(n)
for i in gen:
    print(i)