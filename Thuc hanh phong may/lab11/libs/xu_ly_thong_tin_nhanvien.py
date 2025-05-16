def tinh_luong(he_so):
    return he_so * 1490000

def tinh_phu_cap(chuc_vu):
    if chuc_vu.upper() == 'TP':
        return 1000000
    elif chuc_vu.upper() == 'PP':
        return 700000
    else:
        return 300000

def tinh_thuc_linh(he_so, chuc_vu):
    return tinh_luong(he_so) + tinh_phu_cap(chuc_vu)
