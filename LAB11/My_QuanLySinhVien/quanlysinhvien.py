import csv

class SinhVien:
    def __init__(self, ma, ho_ten, diem_tb, diem_rl):
        self.ma = ma
        self.ho_ten = ho_ten
        self.diem_tb = diem_tb
        self.diem_rl = diem_rl
        self.diem_tl = (diem_tb + diem_rl) / 2

    def to_list(self):
        return [self.ma, self.ho_ten, self.diem_tb, self.diem_rl, self.diem_tl]


def nhap_danh_sach_sv():
    danh_sach = []
    n = int(input("Nhập số lượng sinh viên: "))
    for _ in range(n):
        ma = input("Mã SV: ")
        ho_ten = input("Họ tên: ")
        diem_tb = float(input("Điểm TB: "))
        diem_rl = float(input("Điểm RL: "))
        sv = SinhVien(ma, ho_ten, diem_tb, diem_rl)
        danh_sach.append(sv)
    return danh_sach


def ghi_file_csv(danh_sach, ten_file="My_QuanLySinhVien/files/ds_sinhvien.csv"):
    with open(ten_file, mode='w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(["Mã SV", "Họ tên", "Điểm TB", "Điểm RL", "Điểm TL"])
        for sv in danh_sach:
            writer.writerow(sv.to_list())


def sap_xep_theo_rl(danh_sach):
    return sorted(danh_sach, key=lambda sv: sv.diem_rl)


def tim_max_tl(danh_sach):
    return max(danh_sach, key=lambda sv: sv.diem_tl)