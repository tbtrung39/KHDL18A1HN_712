def tinh_tien_thue_san(gio_bat_dau, gio_ket_thuc):
    if not (5 <= gio_bat_dau <= gio_ket_thuc <= 22):
        return "Giờ nhập không hợp lệ"
    thoi_gian = gio_ket_thuc - gio_bat_dau
    gia_giam = 0.75
    don_gia = 100000
    if thoi_gian <= 3:
        tien = thoi_gian * don_gia
    else:
        tien = 3 * don_gia + (thoi_gian - 3) * don_gia * gia_giam
    if 11 <= gio_bat_dau <= 15:
        tien *= 0.9
    return f"Số tiền phải trả là: {tien:,.0f} đồng"

gio_bat_dau = int(input("Nhập giờ bắt đầu (5-22): "))
gio_ket_thuc = int(input("Nhập giờ kết thúc (5-22): "))
print(tinh_tien_thue_san(gio_bat_dau, gio_ket_thuc))
