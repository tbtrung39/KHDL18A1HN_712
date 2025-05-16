import csv

class SinhVien:
    def __init__(self, ma, ho_ten, diem_tb, diem_rl):
        self.ma = ma
        self.ho_ten = ho_ten
        self.diem_tb = diem_tb
        self.diem_rl = diem_rl
        self.tl = self.tinh_tl()

    def tinh_tl(self):
        return (self.diem_tb + self.diem_rl) / 2

    def __str__(self):
        return f"{self.ma} | {self.ho_ten} | TB: {self.diem_tb} | RL: {self.diem_rl} | TL: {self.tl:.2f}"

def nhap_danh_sach():
    ds = []
    n = int(input("Nhập số lượng sinh viên: "))
    for _ in range(n):
        ma = input("Mã SV: ")
        ho_ten = input("Họ tên: ")
        diem_tb = float(input("Điểm TB: "))
        diem_rl = float(input("Điểm RL: "))
        ds.append(SinhVien(ma, ho_ten, diem_tb, diem_rl))
    return ds

def luu_sinhvien_yeu(ds, filename='ds_sinhvien.csv'):
    with open(filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['MaSV', 'HoTen', 'DiemTB', 'DiemRL', 'DiemTL'])
        for sv in ds:
            if sv.tl < 5.0:
                writer.writerow([sv.ma, sv.ho_ten, sv.diem_tb, sv.diem_rl, f"{sv.tl:.2f}"])

def sap_xep_theo_rl(ds):
    return sorted(ds, key=lambda sv: sv.diem_rl)

def tim_sv_tl_cao_nhat(ds):
    max_tl = max(ds, key=lambda sv: sv.tl).tl
    return [sv for sv in ds if sv.tl == max_tl]
