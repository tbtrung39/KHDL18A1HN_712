t = float(input("Nhập thời gian sử dụng bóng đèn (giây): "))

hieu_dien_the = 220
cuong_do_dien = 2.7
gia_dien = 7000

cong_suat = hieu_dien_the * cuong_do_dien
dien_nang = (cong_suat * t) / (1000 * 3600)  # kWh
tien_dien = dien_nang * gia_dien

print(f"Số tiền điện phải trả: {tien_dien:.2f} đồng")
