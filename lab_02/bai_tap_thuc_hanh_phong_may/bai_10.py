def tinh_tien_thue_san(gio_bat_dau, gio_ket_thuc):
    thoi_gian_thue = gio_ket_thuc - gio_bat_dau
    if thoi_gian_thue <= 0 or gio_bat_dau < 5 or gio_ket_thuc > 22:
        return "Giờ thuê không hợp lệ"

    tien_thue = 0
    if thoi_gian_thue <= 3:
        tien_thue = thoi_gian_thue * 100000
    else:
        tien_thue = 3 * 100000 + (thoi_gian_thue - 3) * 100000 * 0.75

    if 11 <= gio_bat_dau <= 15 or 11 <= gio_ket_thuc <= 15:
        tien_thue *= 0.9

    return tien_thue

gio_bat_dau = int(input("Nhập giờ bắt đầu thuê (5-22): "))
gio_ket_thuc = int(input("Nhập giờ kết thúc thuê (5-22): "))
print(f"Tiền thuê sân là: {tinh_tien_thue_san(gio_bat_dau, gio_ket_thuc)} đồng")