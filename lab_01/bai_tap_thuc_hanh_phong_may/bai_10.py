import math

x = float(input("Nhập giá trị x: "))

log4_x = math.log(x, 4)
logx_2 = math.log(2) / math.log(x)
f = log4_x + logx_2

print(f"Giá trị của biểu thức là: {f:.2f}")
