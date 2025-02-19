import math

r = float(input("Nhập bán kính khối trụ: "))
h = float(input("Nhập chiều cao khối trụ: "))

pi = 3.14
dien_tich_xung_quanh = round(2 * pi * r * h, 2)
dien_tich_toan_phan = round(2 * pi * r * (r + h), 2)
the_tich = round(pi * r**2 * h, 2)

print(f"Diện tích xung quanh: {dien_tich_xung_quanh}")
print(f"Diện tích toàn phần: {dien_tich_toan_phan}")
print(f"Thể tích khối trụ: {the_tich}")
