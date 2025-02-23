bat_dau = int(input("Nhập giờ bắt đầu: "))
ket_thuc = int(input("Nhập giờ kết thúc: "))

if 5 <= bat_dau <= ket_thuc <= 22:
    so_gio = ket_thuc - bat_dau
    if so_gio <= 3:
        tien = so_gio * 100000
    else:
        tien = 3 * 100000 + (so_gio - 3) * (100000 * 0.75)

    if 11 <= bat_dau < 15:
        tien *= 0.9  # Giảm giá 10%

    print(f"Số tiền phải trả: {tien} đồng")
else:
    print("Giờ không hợp lệ!")
