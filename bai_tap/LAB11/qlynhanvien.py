from libs import xu_ly_thong_tin_nhanvien as xl
import os

def nhap_danh_sach_nv():
    ds_nv = []
    so_nv = int(input("Nhập số lượng nhân viên: "))
    for _ in range(so_nv):
        ma = input("Mã NV: ")
        ten = input("Tên NV: ")
        chuc_vu = input("Chức vụ (TP/PP/NV): ")
        he_so = float(input("Hệ số lương: "))
        luong = xl.tinh_luong(he_so)
        phu_cap = xl.tinh_phu_cap(chuc_vu)
        thuc_linh = xl.tinh_thuc_linh(luong, phu_cap)
        ds_nv.append({
            'ma': ma, 'ten': ten, 'chuc_vu': chuc_vu, 'he_so': he_so,
            'luong': luong, 'phu_cap': phu_cap, 'thuc_linh': thuc_linh
        })
    return ds_nv

def in_danh_sach_nv(ds_nv):
    print(f"{'MaNV':<10}{'TenNV':<20}{'ChucVu':<8}{'HeSo':<6}{'Luong':<12}{'PhuCap':<10}{'ThucLinh':<12}")
    for nv in ds_nv:
        print(f"{nv['ma']:<10}{nv['ten']:<20}{nv['chuc_vu']:<8}{nv['he_so']:<6}{nv['luong']:<12,.0f}{nv['phu_cap']:<10,.0f}{nv['thuc_linh']:<12,.0f}")

def main():
    ds_nv = []
    while True:
        print("\nChương trình Quản lý Nhân viên")
        print("1. Nhập danh sách nhân viên")
        print("2. In danh sách nhân viên")
        print("3. Sắp xếp theo thực lĩnh giảm dần")
        print("4. Lưu danh sách vào file")
        print("0. Thoát")
        chon = input("Chọn: ")

        if chon == '1':
            ds_nv = nhap_danh_sach_nv()
        elif chon == '2':
            in_danh_sach_nv(ds_nv)
        elif chon == '3':
            ds_nv = xl.sap_xep_theo_thuc_linh(ds_nv)
            in_danh_sach_nv(ds_nv)
        elif chon == '4':
            filepath = os.path.join('files', 'ds_nhanvien.csv')
            xl.ghi_file(ds_nv, filepath)
            print("Đã lưu vào file.")
        elif chon == '0':
            break
        else:
            print("Lựa chọn không hợp lệ.")

if __name__ == '__main__':
    main()
