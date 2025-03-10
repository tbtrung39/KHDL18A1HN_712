import math
x = float(input("Nhap x: "))
eps = 10**-4
cos_x = 1
term = 1
i = 1
while abs(term) > eps:
    term *= -x**2 / ((2*i-1) * (2*i))
    cos_x += term
    i += 1
print("Gia tri gan dung cua cos(x) =", cos_x)
print("Gia tri thuc te cua cos(x) =", math.cos(x))