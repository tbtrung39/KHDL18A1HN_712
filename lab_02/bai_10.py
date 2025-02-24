gio_bat_dau = int(input("Nhập giờ bắt đầu (5 <= giờ <= 22): "))
gio_ket_thuc = int(input("Nhập giờ kết thúc (5 <= giờ <= 22): "))
thoi_gian_thue = gio_ket_thuc - gio_bat_dau
if thoi_gian_thue < 0:
    print("Giờ kết thúc phải sau giờ bắt đầu!")
else:
    tien_thue = 0

    if thoi_gian_thue <= 3:
        tien_thue = thoi_gian_thue * 100000
    else:
        tien_thue = 3 * 100000 + (thoi_gian_thue - 3) * 75000
    
    if 11 <= gio_bat_dau < 15 or 11 < gio_ket_thuc <= 15:
        tien_thue = tien_thue * 0.9  

    print(f"Số tiền thuê sân là: {tien_thue:,.0f} đồng")