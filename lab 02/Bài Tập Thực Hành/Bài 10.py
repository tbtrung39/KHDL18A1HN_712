gio_bat_dau = int(input("Nhập giờ bắt đầu (5-22): "))
gio_ket_thuc = int(input("Nhập giờ kết thúc (5-22): "))

thoi_gian = gio_ket_thuc - gio_bat_dau
if thoi_gian <= 3:
    tien = thoi_gian * 100000
else:
    tien = 3 * 100000 + (thoi_gian - 3) * 75000

if 11 <= gio_bat_dau <= 15:
    tien = tien * 0.9

print(f"Số tiền phải trả là: {tien} đồng")