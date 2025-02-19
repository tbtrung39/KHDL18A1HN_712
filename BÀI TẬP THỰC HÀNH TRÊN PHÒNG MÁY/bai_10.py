import math
x = float(input("Nhập giá trị x: "))
if x > 0 and x != 1:
 log2_x = math.log2(x) 
 f_x = (log2_x / 2) + (1 / log2_x)
 print("Giá trị của f(x) = %.2f" % f_x)
else:
 print("Giá trị x không hợp lệ. x phải > 0 và ≠ 1.")