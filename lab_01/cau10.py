import math
x = float(input("Nhập giá trị x: "))
log4_x = math.log(x, 4)   # log_4(x) = log(x) / log(4)
logx_2 = math.log(2, x)   # log_x(2) = log(2) / log(x)
f_x = log4_x + logx_2
print("Giá trị của f(x) là:", round(f_x, 2))
