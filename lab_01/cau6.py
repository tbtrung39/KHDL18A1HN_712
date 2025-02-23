hieu_dien_the = 220  
cuong_do_dong = 2.7  
gia_dien = 7000  # đồng/kWh
thoi_gian_s = int(input("Nhập thời gian sử dụng bóng đèn (giây): "))
cong_suat = hieu_dien_the * cuong_do_dong  
thoi_gian_h = thoi_gian_s / 3600  
dien_nang = (cong_suat * thoi_gian_h) / 1000  # Đơn vị: kWh
tien_dien = dien_nang * gia_dien
print("Số tiền điện phải trả là:", round(tien_dien, 2), "đồng")