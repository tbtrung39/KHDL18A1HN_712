def nhap_nhan_vien():
    ho_ten = input("Nhập họ tên: ")
    que_quan = input("Nhập quê quán: ")
    tham_nien = int(input("Nhập thâm niên công tác (năm): "))
    return ho_ten, que_quan, tham_nien

def tinh_luong(tham_nien):
    return 3000000 + tham_nien * 500000  # Lương cơ bản + phụ cấp

def xuat_nhan_vien(ho_ten, que_quan, tham_nien, luong):
    print("Thông tin nhân viên:")
    print(f"Họ tên: {ho_ten}")
    print(f"Quê quán: {que_quan}")
    print(f"Thâm niên: {tham_nien} năm")
    print(f"Lương: {luong} VND")

ho_ten, que_quan, tham_nien = nhap_nhan_vien()
luong = tinh_luong(tham_nien)
xuat_nhan_vien(ho_ten, que_quan, tham_nien, luong)
