# Định nghĩa hằng số pi
PI = 3.14

# Nhập bán kính và chiều cao từ bàn phím
r = float(input("Nhập bán kính của khối trụ: "))
h = float(input("Nhập chiều cao của khối trụ: "))

# Tính diện tích xung quanh (2 * π * r * h)
dien_tich_xq = 2 * PI * r * h

# Tính diện tích toàn phần (diện tích xung quanh + diện tích hai đáy)
dien_tich_tp = dien_tich_xq + 2 * PI * r**2

# Tính thể tích khối trụ (π * r^2 * h)
the_tich = PI * r**2 * h

# Xuất kết quả, làm tròn đến 2 chữ số thập phân
print(f"\nDiện tích xung quanh: {dien_tich_xq:.2f}")
print(f"Diện tích toàn phần: {dien_tich_tp:.2f}")
print(f"Thể tích khối trụ: {the_tich:.2f}")