from libs.Xu_ly_thong_tin_nhan_vien import *
from files import *
import csv
import os

ds_nhanvien = []

def nhap_danh_sach():
    n = int(input("Nhập số lượng nhân viên: "))
    for _ in range(n):
        manv = input("Mã NV: ")
        tennv = input("Tên NV: ")
        chucvu = input("Chức vụ (TP/PP/NV): ")
        heso = float(input("Hệ số lương: "))

        luong = tinh_luong(heso)
        phu_cap = tinh_phu_cap(chucvu)
        thuc_linh = tinh_thuc_linh(heso, chucvu)

        nhanvien = {
            'MaNV': manv,
            'TenNV': tennv,
            'ChucVu': chucvu,
            'HeSo': heso,
            'Luong': luong,
            'PhuCap': phu_cap,
            'ThucLinh': thuc_linh
        }

        ds_nhanvien.append(nhanvien)

def in_danh_sach():
    print("{:<10} {:<20} {:<6} {:<6} {:<10} {:<10} {:<10}".format(
        "MaNV", "TenNV", "CV", "HS", "Luong", "PhuCap", "ThucLinh"
    ))
    for nv in ds_nhanvien:
        print("{:<10} {:<20} {:<6} {:<6} {:<10,.0f} {:<10,.0f} {:<10,.0f}".format(
            nv['MaNV'], nv['TenNV'], nv['ChucVu'], nv['HeSo'],
            nv['Luong'], nv['PhuCap'], nv['ThucLinh']
        ))

def sap_xep_thuc_linh():
    ds_nhanvien.sort(key=lambda x: x['ThucLinh'], reverse=True)

def luu_vao_file():
    os.makedirs('files', exist_ok=True)

    with open('LAB11(BAI_8)/files/ds_nhanvien.csv', 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['MaNV', 'TenNV', 'ChucVu', 'HeSo', 'Luong', 'PhuCap', 'ThucLinh'])
        for nv in ds_nhanvien:
            writer.writerow([
                nv['MaNV'], nv['TenNV'], nv['ChucVu'], nv['HeSo'],
                nv['Luong'], nv['PhuCap'], nv['ThucLinh']
            ])


def menu():
    while True:
        print("\n=== QUẢN LÝ NHÂN VIÊN ===")
        print("1. Nhập danh sách nhân viên")
        print("2. Hiển thị danh sách nhân viên")
        print("3. Sắp xếp theo Thực lĩnh giảm dần")
        print("4. Lưu vào file CSV")
        print("0. Thoát")

        chon = input("Chọn chức năng: ")
        if chon == '1':
            nhap_danh_sach()
        elif chon == '2':
            in_danh_sach()
        elif chon == '3':
            sap_xep_thuc_linh()
            print("Đã sắp xếp.")
        elif chon == '4':
            luu_vao_file()
            print("Đã lưu vào files/ds_nhanvien.csv")
        elif chon == '0':
            break
        else:
            print("Lựa chọn không hợp lệ!")

menu()