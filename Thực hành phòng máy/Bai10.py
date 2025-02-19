import math
x = float(input("Nhập x: "))
log4_x = math.log(x, 4)
logx_2 = math.log(2, x)
f = log4_x + logx_2
print("Giá trị của f(x) là:",round(f,2) )