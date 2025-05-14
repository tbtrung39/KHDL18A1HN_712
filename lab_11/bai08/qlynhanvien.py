import csv
from libs.xu_ly_thong_tin import tinh_luong, tinh_phu_cap, tinh_thuc_linh, in_bang_nv

danh_sach_nv = []
def nhap_nv():
    so_nv = int(input("Nhap so luong nhan vien: "))
    for _ in range(so_nv):
        ma = input("Ma NV: ")
        ten = input("Ten NV: ")
        cv = input("Chuc vu (TP, PP, NV): ").upper()
        hs = float(input("He so luong: "))
        
        luong = tinh_luong(hs)
        pc = tinh_phu_cap(cv)
        thuc_linh = tinh_thuc_linh(luong, pc)

        nv = {
            'ma': ma,
            'ten': ten,
            'cv': cv,
            'hs': hs,
            'luong': luong,
            'pc': pc,
            'thuc_linh': thuc_linh
        }
        danh_sach_nv.append(nv)

def luu_csv():
    path = 'lab_11/bai08/files/ds_nhanvien.csv'
    with open(path, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['Ma NV', 'Ten NV', 'Chuc vu', 'He so luong', 'Luong', 'Phu cap', 'Thuc linh'])
        for nv in danh_sach_nv:
            writer.writerow([nv['ma'], nv['ten'], nv['cv'], nv['hs'], nv['luong'], nv['pc'], nv['thuc_linh']])
    print("Da luu vao ds_nhanvien.csv")

while True:
    print("MENU QUAN LY NHAN VIEN")
    print("\t1. Nhap danh sach nhan vien")
    print("\t2. In danh sach nhan vien")
    print("\t3. Sap xep theo Thuc linh giam dan va in")
    print("\t4. Luu vao file CSV")
    print("\t0. Thoat")
    chon = input("Chon chuc nang: ")

    if chon == '1': nhap_nv()
    elif chon == '2': in_bang_nv(danh_sach_nv)
    elif chon == '3':
        ds_sapxep = sorted(danh_sach_nv, key=lambda nv: nv['thuc_linh'], reverse=True)
        in_bang_nv(ds_sapxep)
    elif chon == '4': luu_csv()
    elif chon == '0':
        print("Thoat chuong trinh")
        break
    else: print("Chon khong hop le")
