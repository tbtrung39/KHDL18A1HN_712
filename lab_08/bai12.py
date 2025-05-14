def nhap_thong_tin_nv():
    ho_ten = input("Nhập họ tên nhân viên: ")
    que_quan = input("Nhập quê quán: ")
    tham_nien = int(input("Nhập thâm niên công tác (năm): "))
    return ho_ten, que_quan, tham_nien

def tinh_luong(tham_nien):
    luong_co_ban = 5000000  
    phu_cap = 200000        
    return luong_co_ban + (tham_nien * phu_cap)

def xuat_thong_tin_nv(ho_ten, que_quan, tham_nien, luong):
    print(f"Họ tên: {ho_ten}")
    print(f"Quê quán: {que_quan}")
    print(f"Thâm niên công tác: {tham_nien} năm")
    print(f"Lương: {luong:,} VNĐ") 
ho_ten, que_quan, tham_nien = nhap_thong_tin_nv()
luong = tinh_luong(tham_nien)
xuat_thong_tin_nv(ho_ten, que_quan, tham_nien, luong)
