import csv
import os

class SinhVien:
    def __init__(self, ma_sv, ho_ten, diem_tb, diem_rl):
        self.ma_sv = ma_sv
        self.ho_ten = ho_ten
        self.diem_tb = float(diem_tb)
        self.diem_rl = float(diem_rl)
        self.diem_tl = self.tinh_diem_tich_luy()
    
    def tinh_diem_tich_luy(self):
        return (self.diem_tb + self.diem_rl) / 2
    
    def __str__(self):
        return f"{self.ma_sv:8} | {self.ho_ten:20} | {self.diem_tb:5.1f} | {self.diem_rl:5.1f} | {self.diem_tl:5.1f}"

class QuanLySinhVien:
    def __init__(self):
        self.danh_sach_sv = []
    
    def nhap_sinh_vien(self):
        n = int(input("Nhập số lượng sinh viên: "))
        for i in range(n):
            print(f"\nNhập thông tin sinh viên thứ {i+1}:")
            ma_sv = input("Mã SV: ")
            ho_ten = input("Họ tên: ")
            diem_tb = float(input("Điểm TB: "))
            diem_rl = float(input("Điểm RL: "))
            sv = SinhVien(ma_sv, ho_ten, diem_tb, diem_rl)
            self.danh_sach_sv.append(sv)
    
    def in_danh_sach(self):
        print("\nDANH SÁCH SINH VIÊN")
        print("-" * 70)
        print("Mã SV    | Họ tên               | Điểm TB | Điểm RL | Điểm TL")
        print("-" * 70)
        for sv in self.danh_sach_sv:
            print(sv)
        print("-" * 70)
    
    def luu_file_csv(self):
        if not os.path.exists('files'):
            os.makedirs('files')
        
        with open('files/ds_sinhvien.csv', 'w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(['Mã SV', 'Họ tên', 'Điểm TB', 'Điểm RL', 'Điểm TL'])
            for sv in self.danh_sach_sv:
                writer.writerow([sv.ma_sv, sv.ho_ten, sv.diem_tb, sv.diem_rl, sv.diem_tl])
        print("\nĐã lưu danh sách sinh viên vào file 'files/ds_sinhvien.csv'")
    
    def sap_xep_theo_diem_rl(self):
        self.danh_sach_sv.sort(key=lambda x: x.diem_rl)
        print("\nĐã sắp xếp danh sách theo điểm rèn luyện tăng dần")
    
    def tim_sv_diem_tl_cao_nhat(self):
        if not self.danh_sach_sv:
            print("Danh sách sinh viên trống!")
            return
        
        max_diem = max(sv.diem_tl for sv in self.danh_sach_sv)
        sv_max = [sv for sv in self.danh_sach_sv if sv.diem_tl == max_diem]
        
        print("\nSINH VIÊN CÓ ĐIỂM TÍCH LŨY CAO NHẤT")
        print("-" * 70)
        print("Mã SV    | Họ tên               | Điểm TB | Điểm RL | Điểm TL")
        print("-" * 70)
        for sv in sv_max:
            print(sv)
        print("-" * 70)