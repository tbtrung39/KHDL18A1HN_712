import csv
import os
from libs import xu_ly_thong_tin_nhanvien as xl

DS_FILE = "files/ds_nhanvien.csv"

def nhap_danh_sach_nv():
    n = int(input("Nhập số lượng nhân viên: "))
    ds_nv = []
    for _ in range(n):
        ma = input("Mã NV: ")
        ten = input("Tên NV: ")
        chuc_vu = input("Chức vụ (TP/PP/NV): ")
        he_so = float(input("Hệ số lương: "))
        phu_cap = xl.tinh_phu_cap(chuc_vu)
        luong = xl.tinh_luong(he_so)
        thuc_linh = xl.tinh_thuc_linh(he_so, chuc_vu)
        ds_nv.append([ma, ten, chuc_vu, he_so, luong, phu_cap, thuc_linh])
    return ds_nv

def ghi_file(ds_nv):
    with open(DS_FILE, mode='w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['MaNV', 'TenNV', 'ChucVu', 'HeSoLuong', 'Luong', 'PhuCap', 'ThucLinh'])
        writer.writerows(ds_nv)

def doc_file():
    ds_nv = []
    if os.path.exists(DS_FILE):
        with open(DS_FILE, mode='r', encoding='utf-8') as f:
            reader = csv.reader(f)
            next(reader)  # bỏ dòng tiêu đề
            for row in reader:
                ds_nv.append(row)
    return ds_nv

def in_danh_sach(ds_nv):
    print(f"{'MaNV':<10}{'TenNV':<20}{'ChucVu':<10}{'HeSo':<6}{'Luong':<12}{'PhuCap':<10}{'ThucLinh':<12}")
    for nv in ds_nv:
        print(f"{nv[0]:<10}{nv[1]:<20}{nv[2]:<10}{nv[3]:<6}{nv[4]:<12}{nv[5]:<10}{nv[6]:<12}")

def sap_xep_theo_thuc_linh(ds_nv):
    return sorted(ds_nv, key=lambda x: float(x[6]), reverse=True)

def menu():
    while True:
        print("\n=== QUẢN LÝ NHÂN VIÊN ===")
        print("1. Nhập danh sách nhân viên")
        print("2. Xem danh sách nhân viên")
        print("3. Sắp xếp theo Thực Lĩnh giảm dần")
        print("4. Thoát")

        chon = input("Chọn chức năng: ")

        if chon == '1':
            ds_nv = nhap_danh_sach_nv()
            ghi_file(ds_nv)
        elif chon == '2':
            ds_nv = doc_file()
            in_danh_sach(ds_nv)
        elif chon == '3':
            ds_nv = doc_file()
            ds_sorted = sap_xep_theo_thuc_linh(ds_nv)
            in_danh_sach(ds_sorted)
        elif chon == '4':
            print("Kết thúc chương trình.")
            break
        else:
            print("Lựa chọn không hợp lệ!")

if __name__ == "__main__":
    menu()
