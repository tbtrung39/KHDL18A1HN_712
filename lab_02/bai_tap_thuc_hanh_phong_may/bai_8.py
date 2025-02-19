def tinh_luong(tham_nien):
    luong_can_ban = 1350000
    if tham_nien < 12:
        he_so = 2.34
    elif 12 <= tham_nien < 36:
        he_so = 3.33
    elif 36 <= tham_nien < 60:
        he_so = 3.66
    else:
        he_so = 3.99
    return he_so * luong_can_ban

tham_nien = int(input("Nhập thâm niên công tác (tháng): "))
print(f"Lương của nhân viên là: {tinh_luong(tham_nien)} đồng")