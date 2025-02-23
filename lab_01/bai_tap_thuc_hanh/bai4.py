import math
x = float(input("Nhập giá trị x: "))
tu_so = -x + math.sqrt(x**2 + 4)
mau_so = 7 * math.sqrt(x**4 + 1)
f_x = tu_so / mau_so
print("Giá trị của f(x) là:", round(f_x, 2))