gio_bat_dau = int(input("Nhập giờ bắt đầu: "))
gio_ket_thuc = int(input("Nhập giờ kết thúc: "))
so_gio = gio_ket_thuc - gio_bat_dau
gia_3_gio_dau = 100000
gia_giam_25 = gia_3_gio_dau * 0.75
if so_gio <= 3:
    tien_thue = so_gio * gia_3_gio_dau
else:
    tien_thue = 3 * gia_3_gio_dau + (so_gio - 3) * gia_giam_25
if gio_bat_dau < 15 and gio_ket_thuc > 11:
    tien_thue = tien_thue * 0.9
print("Số tiền khách phải trả là:", int(tien_thue), "đồng")
