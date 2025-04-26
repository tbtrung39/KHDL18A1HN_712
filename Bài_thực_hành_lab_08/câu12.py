def nhap_nhan_vien():
    ten = input("Nhập họ tên: ")
    que = input("Nhập quê quán: ")
    tham_nien = int(input("Nhập thâm niên công tác (năm): "))
    return ten, que, tham_nien

def tinh_luong(tham_nien):
    luong_cb = 5000000
    return luong_cb + tham_nien * 500000

def xuat_nhan_vien(ten, que, tham_nien, luong):
    print(f"Họ tên: {ten}")
    print(f"Quê quán: {que}")
    print(f"Thâm niên công tác: {tham_nien} năm")
    print(f"Lương: {luong} VND")

ten, que, tham_nien = nhap_nhan_vien()
luong = tinh_luong(tham_nien)
xuat_nhan_vien(ten, que, tham_nien, luong)
