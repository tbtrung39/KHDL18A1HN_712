bat_dau = int(input("Nhập giờ bắt đầu (5-22): "))
ket_thuc = int(input("Nhập giờ kết thúc (5-22): "))

tien = 0
gio_dau = 3
gia_gio_dau = 1000000

if bat_dau >= 5 and ket_thuc <= 22 and bat_dau < ket_thuc:
    for i in range(bat_dau, ket_thuc):
        if i - bat_dau < gio_dau:
            tien += gia_gio_dau
        else:
            tien += gia_gio_dau * 0.75
    if 11 <= bat_dau < 15:
        tien *= 0.9
    print("Số tiền thuê sân:", int(tien), "VNĐ")
else:
    print("Giờ không hợp lệ!")
