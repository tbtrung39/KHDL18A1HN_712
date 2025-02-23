gio_bat_dau = int(input("Nhập giờ bắt đầu: "))
gio_ket_thuc = int(input("Nhập giờ kết thúc: "))
gia_3_gio_dau = 100000
giam_gia_sau_3_gio = 0.75
giam_gia_khung_gio = 0.90
tong_tien = 0
time_thue = gio_ket_thuc - gio_bat_dau

if 5 <= gio_bat_dau <= gio_ket_thuc <= 22:
    if time_thue <= 3:
        tong_tien = time_thue * gia_3_gio_dau
    else:
        tong_tien = 3 * gia_3_gio_dau + (time_thue - 3) * gia_3_gio_dau * giam_gia_sau_3_gio
    if gio_bat_dau < 15 and gio_ket_thuc > 11:
        tong_tien *= giam_gia_khung_gio
    print("Số tiền khách phải trả là:", int(tong_tien), "đồng")
else:
    print("Giờ nhập không hợp lệ. Vui lòng nhập trong khoảng 5 giờ đến 22 giờ.")
