import math
x = float(input("Nhập giá trị x: "))
f = (math.log(x) / math.log(4)) + (math.log(2) / math.log(x))
f = int(f * 100) / 100
print("Giá trị của biểu thức là:", f)
