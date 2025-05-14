# su_dung_matran.py

import Matranvuong

print("--- CHƯƠNG TRÌNH XỬ LÝ MA TRẬN VUÔNG ---")

while True:
    try:
        n = int(input("Nhập kích thước N của ma trận vuông: "))
        if n > 0:
            break
        else:
            print("Kích thước ma trận phải là một số dương.")
    except ValueError:
        print("Vui lòng nhập một số nguyên hợp lệ cho kích thước.")

ma_tran = Matranvuong.nhap_matran(n)

print("\nMa trận bạn vừa nhập:")
Matranvuong.in_matran(ma_tran)

ma_tran_chuyen_vi = Matranvuong.chuyen_vi_matran(ma_tran)
print("\nMa trận chuyển vị:")
Matranvuong.in_matran(ma_tran_chuyen_vi)

if Matranvuong.kiem_tra_doi_xung(ma_tran):
    print("\nMa trận này đối xứng.")
else:
    print("\nMa trận này không đối xứng.")