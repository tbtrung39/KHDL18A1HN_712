def tinh_luong(he_so_luong):
    return he_so_luong * 1490000

def tinh_phu_cap(chuc_vu):
    if chuc_vu == 'TP':
        return 1000000
    elif chuc_vu == 'PP':
        return 700000
    elif chuc_vu == 'NV':
        return 300000
    return 0

def tinh_thuc_linh(luong, phu_cap):
    return luong + phu_cap

def sap_xep_theo_thuc_linh(ds_nv):
    return sorted(ds_nv, key=lambda x: x['thuc_linh'], reverse=True)

def ghi_file(ds_nv, filename):
    with open(filename, 'w', encoding='utf-8') as f:
        f.write('MaNV,TenNV,ChucVu,HeSoLuong,Luong,PhuCap,ThucLinh\n')
        for nv in ds_nv:
            line = f"{nv['ma']},{nv['ten']},{nv['chuc_vu']},{nv['he_so']},{nv['luong']},{nv['phu_cap']},{nv['thuc_linh']}\n"
            f.write(line)