def tao_moi_tu_dien_nhan_vien():
    """Tạo một từ điển rỗng để lưu thông tin nhân viên."""
    return {}

def them_nhan_vien(danh_sach_nv):
    """Thêm thông tin nhân viên mới vào từ điển."""
    while True:
        ma_nv = input("Nhập Mã nhân viên (4 ký tự số): ")
        if ma_nv.isdigit() and len(ma_nv) == 4 and ma_nv not in danh_sach_nv:
            break
        else:
            print("Mã nhân viên phải là 4 ký tự số duy nhất. Vui lòng nhập lại.")
    ho_ten = input("Nhập Họ tên nhân viên (tối đa 20 ký tự): ")
    while len(ho_ten) > 20:
        ho_ten = input("Họ tên quá dài. Vui lòng nhập lại (tối đa 20 ký tự): ")
    while True:
        try:
            nam_sinh = int(input("Nhập Năm sinh: "))
            break
        except ValueError:
            print("Năm sinh không hợp lệ. Vui lòng nhập số nguyên.")
    while True:
        try:
            luong = int(input("Nhập Lương: "))
            break
        except ValueError:
            print("Lương không hợp lệ. Vui lòng nhập số nguyên.")
    danh_sach_nv[ma_nv] = {'ho_ten': ho_ten, 'nam_sinh': nam_sinh, 'luong': luong}
    print(f"Đã thêm nhân viên có mã '{ma_nv}'.")
    return danh_sach_nv

def tim_kiem_nhan_vien(danh_sach_nv, ma_nv_tim):
    """Tìm kiếm thông tin nhân viên theo mã nhân viên."""
    if ma_nv_tim in danh_sach_nv:
        info = danh_sach_nv[ma_nv_tim]
        print(f"Thông tin nhân viên có mã '{ma_nv_tim}':")
        print(f"- Họ tên: {info['ho_ten']}")
        print(f"- Năm sinh: {info['nam_sinh']}")
        print(f"- Lương: {info['luong']}")
    else:
        print(f"Không tìm thấy nhân viên có mã '{ma_nv_tim}'.")

def tang_luong_nhan_vien(danh_sach_nv, ma_nv_tang_luong):
    """Tăng lương cho nhân viên có mã được chỉ định."""
    if ma_nv_tang_luong in danh_sach_nv:
        danh_sach_nv[ma_nv_tang_luong]['luong'] += 1000000
        print(f"Đã tăng lương cho nhân viên có mã '{ma_nv_tang_luong}'. Lương mới: {danh_sach_nv[ma_nv_tang_luong]['luong']}")
    else:
        print(f"Không tìm thấy nhân viên có mã '{ma_nv_tang_luong}'.")
    return danh_sach_nv

def xoa_nhan_vien(danh_sach_nv, ma_nv_xoa):
    """Xóa nhân viên có mã được chỉ định."""
    if ma_nv_xoa in danh_sach_nv:
        del danh_sach_nv[ma_nv_xoa]
        print(f"Đã xóa nhân viên có mã '{ma_nv_xoa}'.")
    else:
        print(f"Không tìm thấy nhân viên có mã '{ma_nv_xoa}'.")
    return danh_sach_nv

def sap_xep_nhan_vien_theo_nam_sinh(danh_sach_nv):
    """Sắp xếp từ điển nhân viên giảm dần theo năm sinh."""
    sorted_nv = sorted(danh_sach_nv.items(), key=lambda item: item[1]['nam_sinh'], reverse=True)
    return dict(sorted_nv)

if __name__ == "__main__":
    danh_sach_nhan_vien = tao_moi_tu_dien_nhan_vien()
    n = int(input("Nhập số lượng nhân viên ban đầu: "))
    for _ in range(n):
        danh_sach_nhan_vien = them_nhan_vien(danh_sach_nhan_vien)

    while True:
        print("\n--- Quản lý Nhân viên ---")
        print("1. Thêm nhân viên")
        print("2. Tìm kiếm nhân viên theo mã")
        print("3. Tăng lương nhân viên theo mã")
        print("4. Xóa nhân viên theo mã")
        print("5. Sắp xếp theo năm sinh (giảm dần)")
        print("6. In danh sách nhân viên")
        print("0. Thoát")

        lua_chon = input("Chọn thao tác: ")

        if lua_chon == '1':
            danh_sach_nhan_vien = them_nhan_vien(danh_sach_nhan_vien)
        elif lua_chon == '2':
            ma_nv_tim = input("Nhập mã nhân viên cần tìm: ")
            tim_kiem_nhan_vien(danh_sach_nhan_vien, ma_nv_tim)
        elif lua_chon == '3':
            ma_nv_tang_luong = input("Nhập mã nhân viên cần tăng lương: ")
            danh_sach_nhan_vien = tang_luong_nhan_vien(danh_sach_nhan_vien, ma_nv_tang_luong)
        elif lua_chon == '4':
            ma_nv_xoa = input("Nhập mã nhân viên cần xóa: ")
            danh_sach_nhan_vien = xoa_nhan_vien(danh_sach_nhan_vien, ma_nv_xoa)
        elif lua_chon == '5':
            danh_sach_nhan_vien = sap_xep_nhan_vien_theo_nam_sinh(danh_sach_nhan_vien)
            print("Đã sắp xếp danh sách nhân viên theo năm sinh giảm dần.")
        elif lua_chon == '6':
            print("\n--- Danh sách nhân viên ---")
            for ma_nv, info in danh_sach_nhan_vien.items():
                print(f"Mã NV: {ma_nv}, Họ tên: {info['ho_ten']}, Năm sinh: {info['nam_sinh']}, Lương: {info['luong']}")
        elif lua_chon == '0':
            print("Thoát chương trình.")
            break
        else:
            print("Lựa chọn không hợp lệ. Vui lòng thử lại.")