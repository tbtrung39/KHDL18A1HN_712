# Câu 10:
gio_bat_dau = int(input("Nhập giờ bắt đầu: "))
gio_ket_thuc = int(input("Nhập giờ kết thúc: "))
if gio_bat_dau < 5 or gio_bat_dau > 22 or gio_ket_thuc < 5 or gio_ket_thuc > 22 or gio_bat_dau >= gio_ket_thuc:
    print("Giờ không hợp lệ hãy nhập lại.")
else:
    so_gio_thue = gio_ket_thuc - gio_bat_dau
    if so_gio_thue <= 3:
        gio_3_gio_dau = so_gio_thue
        gio_con_lai = 0
    else:
        gio_3_gio_dau = 3
        gio_con_lai = so_gio_thue - 3
    gia_1_gio_3_gio_dau = 100000
    gia_1_gio_sau_3_gio = gia_1_gio_3_gio_dau * 0.75  
    tong_tien = gio_3_gio_dau * gia_1_gio_3_gio_dau
    if gio_con_lai > 0:
        tong_tien += gio_con_lai * gia_1_gio_sau_3_gio
    if gio_bat_dau < 15 and gio_ket_thuc > 11:
        tong_tien *= 0.9
    print("số tiền phải trả là:",tong_tien,"VND")

