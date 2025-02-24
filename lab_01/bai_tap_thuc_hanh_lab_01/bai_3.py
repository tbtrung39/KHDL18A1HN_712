import math
x = float(input("Nhập giá trị của x: "))
n = round((-x + math.sqrt(x**2 + 4)) / (x**4 + 1)**(1/7),2)
print("Giá trị của biểu thức là:", n)
