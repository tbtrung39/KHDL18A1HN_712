import math
x = float(input("Nhập giá trị x: "))
f_x = round(math.log(x, 4) + math.log(2, x), 2)
print(f"Giá trị của f(x) là: {f_x}")
