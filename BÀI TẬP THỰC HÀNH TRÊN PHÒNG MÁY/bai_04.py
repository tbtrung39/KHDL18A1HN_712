import math
x = float(input("Nhập giá trị x: "))
f_x = (-x + math.sqrt(x)) / 2 + 4 * (math.sqrt(x) / 4) + 1 / 7
print("Giá trị của biểu thức f(x) =", round(f_x, 2))