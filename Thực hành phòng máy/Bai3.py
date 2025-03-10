x = float(input("Nhập giá trị x (radian): "))
cos_x = 1
term = 1
n = 0
while abs(term) > 1e-4:
    n += 1
    term *= - (x**2) / ((2*n) * (2*n - 1))
    cos_x += term
print("cos(x) ≈", cos_x)
