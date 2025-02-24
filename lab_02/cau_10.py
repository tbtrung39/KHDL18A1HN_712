gio_bat_dau = int(input("Nhập giờ bắt đầu thuê sân (5 <= giờ <= 22): "))
gio_ket_thuc = int(input("Nhập giờ kết thúc thuê sân (5 <= giờ <= 22): "))
so_gio_thue = gio_ket_thuc - gio_bat_dau
if 5 <= gio_bat_dau <= 22 and 5 <= gio_ket_thuc <= 22 and so_gio_thue > 0:
    don_gia_3_gio_dau = 100000
    if so_gio_thue <= 3:
        tien_thue = so_gio_thue * don_gia_3_gio_dau
    else:
        tien_thue = 3 * don_gia_3_gio_dau
        tien_thue += (so_gio_thue - 3) * (don_gia_3_gio_dau * 0.75)
    if 11 <= gio_bat_dau < 15 or 11 <= gio_ket_thuc < 15:
        tien_thue *= 0.9  
    print(f"Số tiền khách phải trả là: {tien_thue:.2f} đồng.")
else:
    print("Giờ bắt đầu và kết thúc không hợp lệ hoặc số giờ thuê không hợp lệ.")
