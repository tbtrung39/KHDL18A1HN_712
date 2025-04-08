import math
x = float(input("Nhap gia tri x(radian)"))
cos_x = 1
term = 1
n = 1
while abs(term) >= math.e -4:
    term = (-1)**n*(x**(2*n))/math.factorial(2*n)
    cos_x += term
    n += 1
print(f"cos({x}) ~ {cos_x}")