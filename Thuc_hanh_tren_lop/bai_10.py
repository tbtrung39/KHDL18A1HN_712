import math
def calculate_f(x):
 if x <= 0:
 return "x phải lớn hơn 0"
 log4_x = math.log(x, 4) # log4(x) = log(x) / log(4)
 logx_2 = math.log(2, x) # logx(2) = log(2) / log(x)
 return round(log4_x + logx_2, 2)
x = float(input("Nhập x: "))
print(f"Giá trị của f(x): {calculate_f(x)}")