import math
x = float(input("Nhập giá trị x: "))
f_x = (-x + math.sqrt(x**2 + 4)) / ((x**4 + 1) ** (1/7))
print("Giá trị của f(x) là: %0.2f"%f_x)
print(f_x)
