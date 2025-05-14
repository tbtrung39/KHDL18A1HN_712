# su_dung_qlyhanghoa.py

import qlyhanghoa

print("--- CHƯƠNG TRÌNH QUẢN LÝ HÀNG HÓA SIÊU THỊ ---")

danh_sach_hang_hoa = []

while True:
    print("\n--- MENU ---")
    print("1. Nhập thông tin mặt hàng")
    print("2. Hiển thị danh sách hàng hóa")
    print("3. Sắp xếp theo Thuế VAT (giảm dần)")
    print("0. Thoát")

    lua_chon = input("Nhập lựa chọn của bạn: ")

    if lua_chon == '1':
        print("\n--- Nhập thông tin mặt hàng ---")
        while True:
            mat_hang = qlyhanghoa.nhap_mat_hang()
            danh_sach_hang_hoa.append(mat_hang)
            tiep_tuc = input("Nhập thêm mặt hàng? (y/n): ").lower()
            if tiep_tuc != 'y':
                break
    elif lua_chon == '2':
        print("\n--- Danh sách hàng hóa ---")
        qlyhanghoa.hien_thi_danh_sach(danh_sach_hang_hoa)
    elif lua_chon == '3':
        print("\n--- Danh sách hàng hóa trước khi sắp xếp ---")
        qlyhanghoa.hien_thi_danh_sach(danh_sach_hang_hoa)
        danh_sach_da_sap_xep = qlyhanghoa.sap_xep_theo_thue(danh_sach_hang_hoa)
        print("\n--- Danh sách hàng hóa sau khi sắp xếp theo Thuế VAT (giảm dần) ---")
        qlyhanghoa.hien_thi_danh_sach(danh_sach_da_sap_xep)
    elif lua_chon == '0':
        print("Thoát chương trình.")
        break
    else:
        print("Lựa chọn không hợp lệ.")