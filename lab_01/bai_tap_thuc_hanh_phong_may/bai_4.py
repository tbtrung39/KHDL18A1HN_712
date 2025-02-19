import math
x = float(input("Nhập giá trị x: "))

f = (-x + math.sqrt(x**2 + 4)) / (math.sqrt(x**4 + 1) + 7)

print(f"Giá trị của f(x) là: {f:.2f}")
