# su_dung_hinhhoc.py

import hinhhoc.my_Triangle
import hinhhoc.my_square

print("--- CHƯƠNG TRÌNH SỬ DỤNG PACKAGE HINH HOC ---")

# Sử dụng module my_Triangle
print("\n--- Tam giác ---")
a = 3
b = 4
c = 5
if hinhhoc.my_Triangle.is_TamGiac(a, b, c):
    print(f"({a}, {b}, {c}) là một tam giác.")
    chu_vi_tg = hinhhoc.my_Triangle.ChuviTamGiac(a, b, c)
    dien_tich_tg = hinhhoc.my_Triangle.S_TamGiac(a, b, c)
    print(f"Chu vi: {chu_vi_tg:.2f}")
    print(f"Diện tích: {dien_tich_tg:.2f}")
else:
    print(f"({a}, {b}, {c}) không phải là một tam giác.")

# Sử dụng module my_square
print("\n--- Hình vuông ---")
canh_hv = 7
dien_tich_hv = hinhhoc.my_square.Dien_tich_hinh_vuong(canh_hv)
chu_vi_hv = hinhhoc.my_square.ChuviHinhvuong(canh_hv)
print(f"Hình vuông có cạnh {canh_hv}:")
print(f"Diện tích: {dien_tich_hv}")
print(f"Chu vi: {chu_vi_hv}")