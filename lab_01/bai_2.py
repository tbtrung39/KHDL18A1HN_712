def doi_don_vi_thoi_gian(s, m, h, d):
    """Đổi đơn vị thời gian."""
    tong_giay = s + m * 60 + h * 3600 + d * 86400
    ngay = tong_giay // 86400
    gio = (tong_giay % 86400) // 3600
    phut = (tong_giay % 3600) // 60
    giay = tong_giay % 60
    return ngay, gio, phut, giay

# Ví dụ sử dụng
ngay, gio, phut, giay = doi_don_vi_thoi_gian(30, 45, 2, 1)
print(f"{ngay} ngày, {gio} giờ, {phut} phút, {giay} giây")