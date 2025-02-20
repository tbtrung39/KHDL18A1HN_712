import math

def tinh_khoi_tru(r, h):
    pi = 3.14
    dien_tich_xq = 2 * pi * r * h
    dien_tich_tp = dien_tich_xq + 2 * pi * r**2
    the_tich = pi * r**2 * h
    return round(dien_tich_xq, 2), round(dien_tich_tp, 2), round(the_tich, 2)

r = float(input("Nhập bán kính r: "))
h = float(input("Nhập chiều cao h: "))

dt_xq, dt_tp, v = tinh_khoi_tru(r, h)
print(f"Diện tích xung quanh: {dt_xq}")
print(f"Diện tích toàn phần: {dt_tp}")
print(f"Thể tích khối trụ: {v}")
