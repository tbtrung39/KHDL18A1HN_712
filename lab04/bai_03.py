import math

x = float(input("Nhập giá trị x (radian): "))

cos_x = 1.0
term = 1.0
n = 2

while abs(term) > 1e-4:
  term = -term * x * x / (n * (n - 1))
  cos_x += term
  n += 2

print(f"cos({x}) ≈ {cos_x}")

# Kiểm tra với hàm cos chuẩn trong thư viện math
print(f"cos({x}) (chuẩn) = {math.cos(x)}")