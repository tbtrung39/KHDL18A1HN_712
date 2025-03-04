x = float(input("Nhập x (radian): "))
eps = 1e-4
cos_x = 1
term = 1
i = 2

while abs(term) > eps:
    term *= - (x ** 2) / (i * (i - 1))
    cos_x += term
    i += 2

print("Giá trị gần đúng của cos(x):", cos_x)