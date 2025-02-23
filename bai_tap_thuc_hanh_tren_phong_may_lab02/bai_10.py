gio_bat_dau = int(input("Nhập giờ bắt đầu: "))
gio_ket_thuc = int(input("Nhập giờ kết thúc: "))

don_gia_3_gio_dau = 100000
don_gia_sau_3_gio = don_gia_3_gio_dau * 0.75
giam_gia_gio_trua = 0.1

if 5 <= gio_bat_dau <= gio_ket_thuc <= 22:
    tong_gio = gio_ket_thuc - gio_bat_dau
    if tong_gio <= 3:
        tong_tien = tong_gio * don_gia_3_gio_dau
    else:
        tong_tien = 3 * don_gia_3_gio_dau + (tong_gio - 3) * don_gia_sau_3_gio
    
    if 11 <= gio_bat_dau < 15 or 11 <= gio_ket_thuc <= 15:
        tong_tien *= (1 - giam_gia_gio_trua)
    
    print(f"Số tiền khách phải trả: {int(tong_tien)}đ")
else:
    print("Giờ nhập không hợp lệ, vui lòng nhập lại trong khoảng từ 5 đến 22 giờ.")