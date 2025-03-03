def tinh_luong_nhan_vien(tnct):
    luong_can_ban = 1350000
    if tnct < 12:
        he_so = 2.34
    elif 12 <= tnct < 36:
        he_so = 3.33
    elif 36 <= tnct < 60:
        he_so = 3.66
    else:
        he_so = 3.99
    return he_so * luong_can_ban