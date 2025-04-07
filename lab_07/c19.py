nhan_vien_dict = {}

def them_nhan_vien():
    ma_nv = input("Nhập mã nhân viên: ")
    ho_ten = input("Nhập họ tên: ")
    nam_sinh = int(input("Nhập năm sinh: "))
    luong = int(input("Nhập lương: "))
    nhan_vien_dict[ma_nv] = {
        "ho_ten": ho_ten,
        "nam_sinh": nam_sinh,
        "luong": luong
    }

def tim_kiem_nv():
    ma_nv = input("Nhập mã nhân viên cần tìm: ")
    if ma_nv in nhan_vien_dict:
        print(nhan_vien_dict[ma_nv])
    else:
        print("Không tìm thấy nhân viên.")

def tang_luong():
    ma_nv = input("Nhập mã nhân viên cần tăng lương: ")
    if ma_nv in nhan_vien_dict:
        nhan_vien_dict[ma_nv]["luong"] += 1000000
        print("Đã tăng lương.")
    else:
        print("Không tìm thấy nhân viên.")

def xoa_nv():
    ma_nv = input("Nhập mã nhân viên cần xóa: ")
    if ma_nv in nhan_vien_dict:
        del nhan_vien_dict[ma_nv]
        print("Đã xóa.")
    else:
        print("Không tìm thấy nhân viên.")

def sap_xep_nam_sinh():
    sap_xep = sorted(nhan_vien_dict.items(), key=lambda x: x[1]["nam_sinh"], reverse=True)
    print("\nDanh sách nhân viên theo năm sinh giảm dần:")
    for ma_nv, info in sap_xep:
        print(f"{ma_nv}: {info}")

# Menu
while True:
    print("\nChọn chức năng:")
    print("1. Thêm nhân viên")
    print("2. Tìm nhân viên")
    print("3. Tăng lương")
    print("4. Xóa nhân viên")
    print("5. Sắp xếp theo năm sinh")
    print("0. Thoát")
    chon = input("Lựa chọn: ")
    if chon == "1":
        them_nhan_vien()
    elif chon == "2":
        tim_kiem_nv()
    elif chon == "3":
        tang_luong()
    elif chon == "4":
        xoa_nv()
    elif chon == "5":
        sap_xep_nam_sinh()
    elif chon == "0":
        break
    else:
        print("Lựa chọn không hợp lệ!")
