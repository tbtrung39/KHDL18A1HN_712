# su_dung_doicoso.py

import doicoso.doicoso1
import doicoso.doicoso2

print("--- CHƯƠNG TRÌNH SỬ DỤNG PACKAGE DOI CO SO ---")

# Sử dụng module doicoso1
print("\n--- Đổi cơ số 1 ---")
so_nguyen = doicoso.doicoso1.nhap_so_nguyen()
print(f"Bạn đã nhập số: {so_nguyen}")
print(f"Hệ nhị phân: {doicoso.doicoso1.sang_nhi_phan(so_nguyen)}")
print(f"Hệ bát phân: {doicoso.doicoso1.sang_bat_phan(so_nguyen)}")
print(f"Hệ thập lục phân: {doicoso.doicoso1.sang_thap_luc_phan(so_nguyen)}")

# Sử dụng module doicoso2
print("\n--- Đổi cơ số 2 ---")
chuoi_so = input("Nhập một chuỗi số để kiểm tra và chuyển đổi: ")
chuoi_loc = doicoso.doicoso2.loai_bo_ky_tu_khong_hop_le(chuoi_so)
print(f"Chuỗi sau khi lọc: {chuoi_loc}")
co_so = doicoso.doicoso2.xac_dinh_co_so(chuoi_so)
print(f"Chuỗi '{chuoi_so}' có thể là: {co_so}")

try:
    co_so_chuyen = int(input("Nhập cơ số muốn chuyển sang 10 (2, 8 hoặc 16): "))
    gia_tri_co_so_10 = doicoso.doicoso2.sang_co_so_10(chuoi_so, co_so_chuyen)
    print(f"Giá trị cơ số 10 của '{chuoi_so}' (cơ số {co_so_chuyen}) là: {gia_tri_co_so_10}")
except ValueError:
    print("Cơ số nhập không hợp lệ.")