def tinh_luong(he_so):
    return he_so * 1490000

def tinh_phu_cap(chuc_vu):
    chuc_vu = chuc_vu.upper()
    if chuc_vu == 'TP':
        return 1000000
    elif chuc_vu == 'PP':
        return 700000
    else:
        return 300000

def tinh_thuc_linh(luong, phu_cap):
    return luong + phu_cap

def in_bang_nv(danh_sach):
    print(f"{'Ma NV':<10}{'Ten NV':<20}{'Chuc vu':<10}{'HS Luong':<10}{'Luong':<15}{'Phu cap':<12}{'Thuc linh':<15}")
    print('-'*90)
    for nv in danh_sach:
        print(f"{nv['ma']:<10}{nv['ten']:<20}{nv['cv']:<10}{nv['hs']:<10}{nv['luong']:<15,.0f}{nv['pc']:<12,.0f}{nv['thuc_linh']:<15,.0f}")