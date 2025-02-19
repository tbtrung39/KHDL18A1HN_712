def tinh_tien_dien(thoi_gian_giay):
    hieu_dien_the = 220  
    cuong_do_dong_dien = 2.7  
    cong_suat = hieu_dien_the * cuong_do_dong_dien 
    nang_luong_kWh = (cong_suat * thoi_gian_giay) / (3600 * 1000)
    tien = nang_luong_kWh * 7000
    return round(tien, 2)
thoi_gian_giay = int(input("Nhập thời gian sử dụng bóng đèn (giây): "))
tien = tinh_tien_dien(thoi_gian_giay)
print(f"Số tiền điện phải trả: {tien} đồng")