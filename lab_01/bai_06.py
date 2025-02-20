def tinh_tien_dien(t):
    hieu_dien_the = 220
    cuong_do_dong = 2.7
    cong_suat = hieu_dien_the * cuong_do_dong  # P = U * I
    nang_luong = (cong_suat * t) / 3600000  # kWh
    tien_dien = nang_luong * 7000
    return round(tien_dien, 2)

t = float(input("Nhập thời gian sử dụng bóng đèn (giây): "))
tien = tinh_tien_dien(t)
print(f"Số tiền điện phải trả: {tien} VND")
