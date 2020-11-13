import math
a=float(input("enter the length of the hight"))
b=float(input("enter the length of the base"))
hypotenuse=(a**2) + (b**2)
print("the longest is", math.sqrt(hypotenuse))
area=0.5 * a * b
print("the area is", area)
print(bin(int(area)))