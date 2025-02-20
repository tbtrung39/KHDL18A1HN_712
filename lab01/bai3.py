#câu3
PI = 3.14
r = float(input("Nhập bán kính đáy khối trụ: "))
h = float(input("Nhập chiều cao khối trụ: "))

# Tính diện tích xung quanh, diện tích toàn phần và thể tích
dien_tich_xung_quanh = 2 * PI * r * h
dien_tich_toan_phan = 2 * PI * r * (r + h)
the_tich = PI * r**2 * h
print(f"\nDiện tích xung quanh: {dien_tich_xung_quanh:.2f}")
print(f"Diện tích toàn phần: {dien_tich_toan_phan:.2f}")
print(f"Thể tích khối trụ: {the_tich:.2f}")
