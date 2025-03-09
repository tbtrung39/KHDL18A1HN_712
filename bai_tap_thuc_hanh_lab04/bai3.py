import math

x = float(input("Nhập giá trị x (radian): "))
eps = 1e-4  # Độ chính xác
cos_x = 1
term = 1
i = 2

while abs(term) > eps:
    term *= -x**2 / (i * (i - 1))
    cos_x += term
    i += 2

print(f"Giá trị gần đúng của cos({x}) là: {cos_x}")
print(f"Giá trị thực tế từ math.cos({x}) là: {math.cos(x)}")