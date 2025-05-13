def tinh_luong(he_so_luong):
    return he_so_luong * 1490000

def phu_cap_cv(chuc_vu):
    if chuc_vu == 'TP':
        return 1000000
    elif chuc_vu == 'PP':
        return 700000
    elif chuc_vu == 'NV':
        return 300000
    else:
        return 0

def tinh_thuc_linh(he_so_luong, chuc_vu):
    return tinh_luong(he_so_luong) + phu_cap_cv(chuc_vu)