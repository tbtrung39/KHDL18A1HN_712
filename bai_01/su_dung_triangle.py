# su_dung_triangle.py

import my_Triangle

print("--- CHƯƠNG TRÌNH TÍNH TOÁN VỀ TAM GIÁC ---")

while True:
    try:
        canh_a = float(input("Nhập độ dài cạnh a: "))
        canh_b = float(input("Nhập độ dài cạnh b: "))
        canh_c = float(input("Nhập độ dài cạnh c: "))
        break
    except ValueError:
        print("Vui lòng nhập số hợp lệ cho độ dài cạnh.")

if my_Triangle.is_TamGiac(canh_a, canh_b, canh_c):
    print("\nĐây là một tam giác hợp lệ.")
    chu_vi = my_Triangle.ChuviTamGiac(canh_a, canh_b, canh_c)
    dien_tich = my_Triangle.S_TamGiac(canh_a, canh_b, canh_c)
    print(f"Chu vi của tam giác là: {chu_vi:.2f}")
    print(f"Diện tích của tam giác là: {dien_tich:.2f}")
else:
    print("\nBa cạnh đã nhập không tạo thành một tam giác.")
    thong_bao_chu_vi = my_Triangle.ChuviTamGiac(canh_a, canh_b, canh_c)
    thong_bao_dien_tich = my_Triangle.S_TamGiac(canh_a, canh_b, canh_c)
    if isinstance(thong_bao_chu_vi, str):
        print(f"Thông báo về chu vi: {thong_bao_chu_vi}")
    if isinstance(thong_bao_dien_tich, str):
        print(f"Thông báo về diện tích: {thong_bao_dien_tich}")