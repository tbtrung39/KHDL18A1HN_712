# Khai báo các biến
hieu_dien_the = 220  # V
cuong_do_dong_dien = 2.7  # A
gia_dien = 7000  # đ/kWh

# Nhập thời gian sử dụng từ người dùng (giây)
thoi_gian_su_dung_giay = int(input("Nhập thời gian sử dụng bóng đèn (giây): "))

# Tính công suất của bóng đèn (W)
cong_suat = hieu_dien_the * cuong_do_dong_dien

# Tính thời gian sử dụng theo giờ
thoi_gian_su_dung_gio = thoi_gian_su_dung_giay / 3600

# Tính điện năng tiêu thụ (kWh)
dien_nang_tieu_thu = (cong_suat / 1000) * thoi_gian_su_dung_gio

# Tính tiền điện phải trả
tien_dien = dien_nang_tieu_thu * gia_dien

# In kết quả
print("Công suất của bóng đèn là:", cong_suat, "W")
print("Điện năng tiêu thụ là:", dien_nang_tieu_thu, "kWh")
print("Tiền điện phải trả là:", round(tien_dien, 2), "đ")