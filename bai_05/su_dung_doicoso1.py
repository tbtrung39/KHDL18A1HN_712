# su_dung_doicoso1.py

import doicoso1

print("--- CHƯƠNG TRÌNH ĐỔI CƠ SỐ ---")

so_nguyen = doicoso1.nhap_so_nguyen()
print(f"Bạn đã nhập số: {so_nguyen}")
print(f"Hệ nhị phân: {doicoso1.sang_nhi_phan(so_nguyen)}")
print(f"Hệ bát phân: {doicoso1.sang_bat_phan(so_nguyen)}")
print(f"Hệ thập lục phân: {doicoso1.sang_thap_luc_phan(so_nguyen)}")