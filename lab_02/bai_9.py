def tinh_tien_dien(so_kw):
    if 0 <= so_kw <= 100:
        return so_kw * 2000
    elif 101 <= so_kw <= 200:
        return 100 * 2000 + (so_kw - 100) * 2500
    elif 201 <= so_kw <= 300:
        return 100 * 2000 + 100 * 2500 + (so_kw - 200) * 3000
    else:
        return 100 * 2000 + 100 * 2500 + 100 * 3000 + (so_kw - 300) * 5000