# Cau 1.

import math
def la_so(x):
    try:
        float(x)
        return True
    except ValueError:
        return False
def la_tam_giac(a, b, c):
    return a + b > c and a + c > b and b + c > a
def tinh_dien_tich_tam_giac(a, b, c):
    p = (a + b + c) / 2
    dien_tich = math.sqrt(p * (p - a) * (p - b) * (p - c))
    return dien_tich
def nhap_canh_tam_giac():
    ds_canh = []
    for i in range(1, 4):
        canh = input(f"Nhap do dai canh thu {i}: ")
        if not la_so(canh):
            raise ValueError(f"Gia tri '{canh}' khong phai la kieu so.")
        canh = float(canh)
        if canh <= 0:
            raise ValueError(f"Gia tri '{canh}' phai lon hon 0.")
        ds_canh.append(canh)
    a, b, c = ds_canh
    if not la_tam_giac(a, b, c):
        raise ValueError(f"Ba canh {a}, {b}, {c} khong thoa man dieu kien tam giac.")
    return a, b, c
try:
    a, b, c = nhap_canh_tam_giac()
    s = tinh_dien_tich_tam_giac(a, b, c)
    print(f"Dien tich tam giac la: {s:.2f}")
except ValueError as e:
    print("Loi:", e)
