
from doicoso import *

def main():
    print("=== Đổi cơ số từ số nguyên ===")
    so = nhap_so_nguyen()
    print("Hệ nhị phân:", doi_sang_nhi_phan(so))
    print("Hệ bát phân:", doi_sang_bat_phan(so))
    print("Hệ thập lục phân:", doi_sang_thap_luc_phan(so))

    print("\n=== Phân tích chuỗi số ===")
    s = input("Nhập chuỗi ký tự: ")
    s_loc = loc_chuoi_16(s)
    print("Chuỗi sau khi loại bỏ ký tự không hợp lệ:", s_loc)

    coso = xac_dinh_co_so(s_loc)
    print("Chuỗi thuộc hệ cơ số:", coso)

    if coso == 2:
        print("Giá trị thập phân:", doi_co_so_2_sang_10(s_loc))
    elif coso == 8:
        print("Giá trị thập phân:", doi_co_so_8_sang_10(s_loc))
    elif coso == 16:
        print("Giá trị thập phân:", doi_co_so_16_sang_10(s_loc))
    else:
        print("Không xác định được hệ cơ số hợp lệ.")
main()
