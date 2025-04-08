import math
x = float(input("Nhập giá trị x: "))
f = (-x + math.sqrt(x**2 + 4)) / ((x**4 + 1) ** (1/7))
f = int(f * 100) / 100  
print("Giá trị của biểu thức là:", f)
