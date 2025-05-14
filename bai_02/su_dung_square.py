# su_dung_square.py

import my_square

print("--- CHƯƠNG TRÌNH TÍNH TOÁN VỀ HÌNH VUÔNG ---")

while True:
    try:
        canh = float(input("Nhập độ dài cạnh của hình vuông: "))
        break
    except ValueError:
        print("Vui lòng nhập một số hợp lệ cho độ dài cạnh.")

chu_vi = my_square.ChuviHinhvuong(canh)
dien_tich = my_square.Dien_tich_hinh_vuong(canh)

print(f"\nHình vuông có cạnh = {canh}:")
print(f"Chu vi = {chu_vi}")
print(f"Diện tích = {dien_tich}")