# Khai báo giá trị pi
pi = 3.14

# Nhập bán kính và chiều cao từ người dùng
ban_kinh = float(input("Nhập bán kính hình trụ: "))
chieu_cao = float(input("Nhập chiều cao hình trụ: "))

# Tính diện tích xung quanh
dien_tich_xung_quanh = 2 * pi * ban_kinh * chieu_cao

# Tính diện tích toàn phần
dien_tich_toan_phan = 2 * pi * ban_kinh * (ban_kinh + chieu_cao)

# Tính thể tích
the_tich = pi * ban_kinh**2 * chieu_cao

# In kết quả đã làm tròn đến hai chữ số thập phân
print("Diện tích xung quanh:", round(dien_tich_xung_quanh, 2))
print("Diện tích toàn phần:", round(dien_tich_toan_phan, 2))
print("Thể tích:", round(the_tich, 2))