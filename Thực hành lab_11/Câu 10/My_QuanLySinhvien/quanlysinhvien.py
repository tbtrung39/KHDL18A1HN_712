import csv
import os

def nhap_danh_sach_sinh_vien():
    ds_sinh_vien = []
    try:
        n = int(input("Nhập số lượng sinh viên: "))
        for i in range(n):
            print(f"\nNhập thông tin sinh viên thứ {i+1}:")
            ma_sv = input("Mã SV: ").strip()
            ho_ten = input("Họ tên: ").strip()
            while True:
                try:
                    diem_tb = float(input("Điểm TB: "))
                    if 0 <= diem_tb <= 10:
                        break
                    print("Điểm TB phải từ 0 đến 10!")
                except ValueError:
                    print("Vui lòng nhập số hợp lệ!")
            while True:
                try:
                    diem_rl = float(input("Điểm RL: "))
                    if 0 <= diem_rl <= 10:
                        break
                    print("Điểm RL phải từ 0 đến 10!")
                except ValueError:
                    print("Vui lòng nhập số hợp lệ!")
            sinh_vien = {
                'ma_sv': ma_sv,
                'ho_ten': ho_ten,
                'diem_tb': diem_tb,
                'diem_rl': diem_rl,
                'diem_tl': 0
            }
            ds_sinh_vien.append(sinh_vien)
        return ds_sinh_vien
    except ValueError:
        print("Số lượng sinh viên phải là số nguyên!")
        return []

def tinh_diem_tl(ds_sinh_vien):
    for sv in ds_sinh_vien:
        sv['diem_tl'] = (sv['diem_tb'] + sv['diem_rl']) / 2
    print("\nĐã tính điểm tích lũy cho tất cả sinh viên!")

def in_danh_sach_sinh_vien(ds_sinh_vien):
    if not ds_sinh_vien:
        print("\nDanh sách sinh viên trống!")
        return
    print("\nDANH SÁCH SINH VIÊN")
    print("-" * 70)
    print("{:<8} | {:<20} | {:>7} | {:>7} | {:>7}".format("Mã SV", "Họ tên", "Điểm TB", "Điểm RL", "Điểm TL"))
    print("-" * 70)
    for sv in ds_sinh_vien:
        print("{:<8} | {:<20} | {:>7.1f} | {:>7.1f} | {:>7.1f}".format(
            sv['ma_sv'], sv['ho_ten'], sv['diem_tb'], sv['diem_rl'], sv['diem_tl']))
    print("-" * 70)

def luu_file_csv(ds_sinh_vien):
    file_path = input("Nhập đường dẫn để lưu file CSV (ví dụ: files/ds_sinhvien.csv): ").strip()
    if not file_path:
        print("Đường dẫn không được để trống!")
        return

    directory = os.path.dirname(file_path)
    if directory and not os.path.exists(directory):
        try:
            os.makedirs(directory, exist_ok=True)
        except Exception as e:
            print(f"Lỗi khi tạo thư mục: {e}")
            return
    if not ds_sinh_vien:
        print("Cảnh báo: Danh sách sinh viên trống, file CSV sẽ chỉ chứa tiêu đề!")
    try:
        with open(file_path, 'w', newline='', encoding='utf-8-sig') as file:
            writer = csv.writer(file)
            writer.writerow(['Mã SV', 'Họ tênUx', 'Điểm TB', 'Điểm RL', 'Điểm TL'])
            for sv in ds_sinh_vien:
                writer.writerow([
                    sv['ma_sv'], sv['ho_ten'], sv['diem_tb'], sv['diem_rl'], sv['diem_tl']
                ])
        print(f"Danh sách đã được lưu vào {os.path.abspath(file_path)}")
    except PermissionError:
        print(f"Lỗi: Không có quyền ghi file vào {file_path}")
    except Exception as e:
        print(f"Lỗi khi lưu file: {e}")

def sap_xep_theo_diem_rl(ds_sinh_vien):
    ds_sinh_vien.sort(key=lambda sv: sv['diem_rl'])
    print("\nĐã sắp xếp danh sách theo điểm rèn luyện tăng dần")

def tim_sinh_vien_diem_tl_cao_nhat(ds_sinh_vien):
    if not ds_sinh_vien:
        print("\nDanh sách sinh viên trống!")
        return
    max_diem = max(sv['diem_tl'] for sv in ds_sinh_vien)
    sv_max = [sv for sv in ds_sinh_vien if sv['diem_tl'] == max_diem]
    print("\nSINH VIÊN CÓ ĐIỂM TÍCH LŨY CAO NHẤT")
    print("-" * 70)
    print("{:<8} | {:<20} | {:>7} | {:>7} | {:>7}".format("Mã SV", "Họ tên", "Điểm TB", "Điểm RL", "Điểm TL"))
    print("-" * 70)
    for sv in sv_max:
        print("{:<8} | {:<20} | {:>7.1f} | {:>7.1f} | {:>7.1f}".format(
            sv['ma_sv'], sv['ho_ten'], sv['diem_tb'], sv['diem_rl'], sv['diem_tl']))
    print("-" * 70)