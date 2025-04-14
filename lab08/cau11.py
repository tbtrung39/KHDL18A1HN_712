def tinh_luong(nam_ct):
    return nam_ct * 12000000  # Ví dụ: 12 triệu mỗi năm

def xuat_nv(ten, que, nam):
    luong = tinh_luong(nam)
    print(f"Tên: {ten}, Quê quán: {que}, Năm công tác: {nam}, Lương: {luong}đ")

ten = input("Nhập tên nhân viên: ")
que = input("Nhập quê quán: ")
nam = int(input("Nhập số năm công tác: "))
xuat_nv(ten, que, nam)