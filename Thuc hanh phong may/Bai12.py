def nhap_nhan_vien():
    ho_ten = input("Nhập họ tên nhân viên: ")
    que_quan = input("Nhập quê quán: ")
    tham_nien = int(input("Nhập thâm niên công tác (năm): "))
    return ho_ten, que_quan, tham_nien
def tinh_luong(tham_nien):
    luong_co_ban = 5000000
    he_so = 0.1 
    luong = luong_co_ban + luong_co_ban * he_so * tham_nien
    return luong
def xuat_nhan_vien(ho_ten, que_quan, tham_nien, luong):
    print(f"Họ tên: {ho_ten}")
    print(f"Quê quán: {que_quan}")
    print(f"Thâm niên công tác: {tham_nien} năm")
    print(f"Lương: {luong:,.0f} VND")
ho_ten, que_quan, tham_nien = nhap_nhan_vien()
luong = tinh_luong(tham_nien)
xuat_nhan_vien(ho_ten, que_quan, tham_nien, luong)
