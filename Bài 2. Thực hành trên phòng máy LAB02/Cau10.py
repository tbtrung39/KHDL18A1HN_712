# Cau 10.
gio_bat_dau = int(input("Nhập vào giờ bắt đầu (5 <= giờ bắt đầu <= 22): "))
gio_ket_thuc = int(input("Nhập vào giờ kết thúc (5 <= giờ kết thúc <= 22): "))

if 5 <= gio_bat_dau <= gio_ket_thuc <= 22:
    thoi_gian_thue = gio_ket_thuc - gio_bat_dau
    gia_gio_dau = 100000
    giam_gia_gio_tiep_theo = 0.25
    giam_gia_khung_gio = 0.1

    if thoi_gian_thue <= 3:
        tong_tien = thoi_gian_thue * gia_gio_dau
    else:
        tien_3_gio_dau = 3 * gia_gio_dau
        tien_gio_tiep_theo = (thoi_gian_thue - 3) * (gia_gio_dau * (1 - giam_gia_gio_tiep_theo))
        tong_tien = tien_3_gio_dau + tien_gio_tiep_theo
    if gio_bat_dau < 15 and gio_ket_thuc > 11:
        tong_tien *= (1 - giam_gia_khung_gio)

    print(f"Số tiền khách thuê sân tập phải trả là: {tong_tien} đồng")
else:
    print("Vui lòng nhập giờ bắt đầu và giờ kết thúc hợp lệ (5 <= giờ bắt đầu <= giờ kết thúc <= 22)")
