import math

n = int(input("Input number of sides: "))
length = int(input("Input the length of sides: "))
area = (n * length**2) / (4 * math.tan(math.pi/n))
print("The area of the polygon is:" + str(round(area)))
