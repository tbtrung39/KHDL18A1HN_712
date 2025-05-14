# su_dung_sohoc.py

import sohoc

print("--- CHƯƠNG TRÌNH TÍNH ƯCLN VÀ BCNN ---")

while True:
    try:
        so1 = int(input("Nhập số nguyên thứ nhất: "))
        so2 = int(input("Nhập số nguyên thứ hai: "))
        break
    except ValueError:
        print("Vui lòng nhập số nguyên hợp lệ.")

ucln = sohoc.Ucln(so1, so2)
bcnn = sohoc.Bcnn(so1, so2)

print(f"\nƯCLN của {so1} và {so2} là: {ucln}")
print(f"BCNN của {so1} và {so2} là: {bcnn}")