# Nhập giờ bắt đầu và giờ kết thúc
gio_bd = int(input("Nhập giờ bắt đầu (5 ≤ giờ ≤ 22): "))
gio_kt = int(input("Nhập giờ kết thúc (5 ≤ giờ ≤ 22): "))

# Kiểm tra điều kiện hợp lệ
if gio_bd < 5 or gio_kt > 22 or gio_bd >= gio_kt:
    print("Giờ nhập không hợp lệ!")
else:
    tong_so_gio = gio_kt - gio_bd  # Tổng số giờ thuê sân
    gia_ba_gio_dau_tien = 10000000 # Giá 3 giờ đầu tiên (VNĐ/giờ)
    gia_sau_ba_gio_dau = gia_ba_gio_dau_tien * 0.75  # Giá sau 3 giờ đầu (giảm 25%)

    # Tính tiền thuê sân
    if tong_so_gio <= 3:
        tong_chi_phi = tong_so_gio * gia_ba_gio_dau_tien
    else:
        tong_chi_phi = 3 * gia_ba_gio_dau_tien + (tong_so_gio - 3) * gia_sau_ba_gio_dau

    # Giảm giá 10% nếu thuê trong khoảng 11h - 15h
    if gio_bd < 15 and gio_kt > 11:
        tong_chi_phi *= 0.9

    # In kết quả
    print(f"Tổng số tiền thuê sân: {round(tong_chi_phi, 2)} VNĐ")
