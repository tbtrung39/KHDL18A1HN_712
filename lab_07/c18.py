# Dữ liệu: từ điển với key là số báo danh
sinh_vien_dict = {}

def nhap_du_lieu():
    n = int(input("Nhập số lượng sinh viên: "))
    for _ in range(n):
        sbd = input("Nhập số báo danh: ")
        ho_ten = input("Nhập họ tên: ")
        diem = float(input("Nhập điểm: "))
        sinh_vien_dict[sbd] = {"ho_ten": ho_ten, "diem": diem}

def tra_cuu():
    sbd = input("Nhập số báo danh cần tra cứu: ")
    if sbd in sinh_vien_dict:
        print("Thông tin sinh viên:")
        print(sinh_vien_dict[sbd])
    else:
        print("Không tìm thấy sinh viên!")

# Demo
nhap_du_lieu()
tra_cuu()
