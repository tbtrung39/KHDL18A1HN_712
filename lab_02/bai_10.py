def tinh_tien_thue_san_bong(gio_bat_dau, gio_ket_thuc):
    thoi_gian_thue = gio_ket_thuc - gio_bat_dau
    if thoi_gian_thue <= 3:
        tien = thoi_gian_thue * 100000
    else:
        tien = 3 * 100000 + (thoi_gian_thue - 3) * 100000 * 0.75
    if 11 <= gio_bat_dau <= 15:
        tien *= 0.9
    return tien