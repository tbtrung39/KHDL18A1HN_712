import math

x = float(input("Nhập x: "))

if x > 0 and x != 1:
    f_x = math.log(x, 4) + math.log(2, x)
    print("Giá trị của f(x):", round(f_x, 2))
else:
    print("Giá trị x không hợp lệ.")
