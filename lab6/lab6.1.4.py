import math
import time
def sqrt(num):
    return math.sqrt(num)
# 500 ml = 0.5 sec
ms = (int(input("Введите время замедления в милисекундах: ")))
s = ms / 1000
n = int(input("Введите число: "))
time.sleep(s)
res = sqrt(n)
print(f"Square root of {n} is:", int(res))
