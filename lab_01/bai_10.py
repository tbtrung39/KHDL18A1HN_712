import math
x = float(input("Nhập giá trị x: "))
log4_x = math.log(x) / math.log(4)
logx_2 = math.log(2) / math.log(x)
f_x = log4_x + logx_2
print("Giá trị của f(x) là:%0.2f" % f_x)