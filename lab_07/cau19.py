nv={}
n=int(input("Nhập vào số lượng nhân viên:"))
for i in range(n):
    ma_nv=int(input("Nhập vào mã nhân viên(gồm 4 chữ số):"))
    ho_ten_nv=input("Nhập vào họ tên nhân viên:")
    nam_sinh=int(input("Nhập vào năm sinh của nhân viên:"))
    luong=int(input("Nhập vào lương của nhân viên:"))
    nv[ma_nv]={
        "họ tên nhân viên": ho_ten_nv,
        "năm sinh của nhân viên": nam_sinh,
        "lương nhân viên": luong
    }
ma_tim=input("Nhập mã nhân viên cần tìm:")
if ma_tim in nv:
    print("thông tin nhân viên:",nv[ma_tim])
else:
    print("Không tìm thấy nhân viên")  

ma_tang_luong=input("Nhập mã nhân viên cần tăng lương:")
if ma_tang_luong in nv:
    nv[ma_tang_luong]["lương nhân viên"] += 100000
    print("Lương mới của nhân viên:", nv[ma_tang_luong]["lương nhân viên"])
else:
    print("Không tìm thấy nhân viên")

ma_xoa = input("Nhập mã nhân viên xóa: ")
if ma_xoa in nv:
    del nv[ma_xoa]
    print("Đã xóa nhân viên")
else:
    print("Không tìm thấy nhân viên")