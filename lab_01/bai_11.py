def tinh_xac_suat_xuc_sac(n):
    """Tính xác suất tung xúc sắc."""
    xac_suat_mot_lan = 1 - (215 / 216)**n
    return round(xac_suat_mot_lan, 2)

# Ví dụ sử dụng
n = 3
print(f"Xác suất: {tinh_xac_suat_xuc_sac(n)}")