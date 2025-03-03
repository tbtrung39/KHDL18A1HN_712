import math

def tinh_khoi_tru(ban_kinh, chieu_cao):
    """Tính diện tích và thể tích khối trụ."""
    dien_tich_xq = 2 * math.pi * ban_kinh * chieu_cao
    dien_tich_tp = dien_tich_xq + 2 * math.pi * ban_kinh**2
    the_tich = math.pi * ban_kinh**2 * chieu_cao
    return round(dien_tich_xq, 2), round(dien_tich_tp, 2), round(the_tich, 2)

# Ví dụ sử dụng
dt_xq, dt_tp, the_tich = tinh_khoi_tru(5, 10)
print(f"Diện tích xung quanh: {dt_xq}, diện tích toàn phần: {dt_tp}, thể tích: {the_tich}")