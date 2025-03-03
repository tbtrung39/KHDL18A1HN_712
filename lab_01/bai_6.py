def tinh_tien_dien(thoi_gian):
    """Tính tiền điện bóng đèn."""
    cong_suat = 220 * 2.7 / 1000  # kWh
    dien_nang = cong_suat * thoi_gian / 3600  # kWh
    tien_dien = dien_nang * 7000
    return tien_dien

# Ví dụ sử dụng
thoi_gian = 3600  # 1 giờ
print(f"Tiền điện: {tinh_tien_dien(thoi_gian)} đồng")