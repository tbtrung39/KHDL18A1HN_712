import math
x = float(input("Nhập giá trị x (radian): "))
epsilon = 1e-4
cos_x = 1
term = 1
n = 1
while abs(term) >= epsilon:
    term *= -x**2 / ((2*n - 1) * (2*n))
    cos_x += term
    n += 1
print("Giá trị gần đúng của cos(x):", cos_x)
print("Giá trị cos(x) theo math.cos:", math.cos(x))