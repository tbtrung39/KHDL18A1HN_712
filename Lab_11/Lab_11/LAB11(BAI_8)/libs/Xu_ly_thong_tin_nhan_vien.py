def tinh_luong(heso):
    return heso * 1490000

def tinh_phu_cap(chucvu):
    if chucvu.upper() == "TP":
        return 1000000
    elif chucvu.upper() == "PP":
        return 700000
    else:
        return 300000

def tinh_thuc_linh(heso, chucvu):
    return tinh_luong(heso) + tinh_phu_cap(chucvu)
