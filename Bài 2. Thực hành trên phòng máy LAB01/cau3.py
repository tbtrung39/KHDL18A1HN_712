r = float(input("Nhập bán kính: "))
h = float(input("Nhập chiều cao: "))
pi = 3.14

dien_tich_xq = 2 * pi * r * h
dien_tich_tp = dien_tich_xq + 2 * pi * r**2
the_tich = pi * r**2 * h

print(f"Diện tích xung quanh: {dien_tich_xq:.2f}")
print(f"Diện tích toàn phần: {dien_tich_tp:.2f}")
print(f"Thể tích khối trụ: {the_tich:.2f}")