import csv
import os

LUONG_CO_BAN = 1490000
FILE_PATH = os.path.join("files", "ds_nhanvien.csv")

def tinh_phu_cap(chuc_vu):
    chuc_vu = chuc_vu.upper()
    if chuc_vu == "TP":
        return 1000000
    elif chuc_vu == "PP":
        return 700000
    elif chuc_vu == "NV":
        return 300000
    else:
        return 0

def tinh_luong(he_so):
    return he_so * LUONG_CO_BAN

def tinh_thuc_linh(he_so, chuc_vu):
    return tinh_luong(he_so) + tinh_phu_cap(chuc_vu)

def nhap_danh_sach():
    ds = []
    while True:
        ma = input("Nhập mã nhân viên: ").strip()
        if not ma:
            print("Mã nhân viên không được để trống."); continue

        ten = input("Nhập tên nhân viên: ").strip()
        if not ten:
            print("Tên nhân viên không được để trống."); continue

        chuc_vu = input("Nhập chức vụ (TP/PP/NV): ").strip().upper()
        if chuc_vu not in ["TP", "PP", "NV"]:
            print("Chức vụ không hợp lệ."); continue

        try:
            he_so = float(input("Nhập hệ số lương: "))
            if he_so <= 0:
                raise ValueError
        except ValueError:
            print("Hệ số lương phải là số dương."); continue

        nv = {
            "MaNV": ma,
            "TenNV": ten,
            "ChucVu": chuc_vu,
            "HeSoLuong": he_so,
            "Luong": tinh_luong(he_so),
            "PhuCap": tinh_phu_cap(chuc_vu),
            "ThucLinh": tinh_thuc_linh(he_so, chuc_vu)
        }
        ds.append(nv)

        tiep = input("Bạn có muốn nhập tiếp? (y/n): ").strip().lower()
        if tiep != "y":
            break
    return ds

def hien_thi_danh_sach(ds):
    print("\n{:<10}{:<20}{:<8}{:<12}{:<10}{:<12}{:<12}".format(
        "MaNV", "TenNV", "ChucVu", "HeSoLuong", "Luong", "PhuCap", "ThucLinh"))
    print("-" * 90)
    for nv in ds:
        print("{:<10}{:<20}{:<8}{:<12.2f}{:<10,.0f}{:<12,.0f}{:<12,.0f}".format(
            nv['MaNV'], nv['TenNV'], nv['ChucVu'], nv['HeSoLuong'],
            nv['Luong'], nv['PhuCap'], nv['ThucLinh']
        ))

def luu_vao_csv(ds):
    path = input("Nhập đường dẫn lưu file CSV (VD: files/ds_nhanvien.csv): ").strip()
    if not path.endswith(".csv"):
        print(" Đường dẫn không hợp lệ. Đường dẫn phải kết thúc bằng '.csv'")
        return

    try:
        os.makedirs(os.path.dirname(path), exist_ok=True)
        with open(path, mode='w', newline='', encoding='utf-8') as f:
            fieldnames = ["MaNV", "TenNV", "ChucVu", "HeSoLuong", "Luong", "PhuCap", "ThucLinh"]
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            for nv in ds:
                writer.writerow(nv)
        print(f"\n Đã lưu danh sách vào '{path}'.")
    except Exception as e:
        print(f" Lỗi khi lưu file: {e}")