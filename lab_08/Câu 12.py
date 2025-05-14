#Câu 12:
def nhap_thong_tin():
    ten = input("Nhập họ tên: ")
    que = input("Nhập quê quán: ")
    tham_nien = int(input("Nhập thâm niên công tác (năm): "))
    return ten, que, tham_nien
def tinh_luong(tham_nien):
    return tham_nien * 1500000
def xuat_thong_tin(ten, que, tham_nien, luong):
    print("\n ======== THÔNG TIN NHÂN VIÊN ==========")
    print("Họ tên:", ten)
    print("Quê quán:", que)
    print("Thâm niên công tác:", tham_nien, "năm")
    print("Lương:", luong, "VND")
ten, que, tham_nien = nhap_thong_tin()
luong = tinh_luong(tham_nien)
xuat_thong_tin(ten, que, tham_nien, luong)