import csv

class SinhVien:
    def __init__(self, ma, ho_ten, diem_tb, diem_rl):
        self.ma = ma
        self.ho_ten = ho_ten
        self.diem_tb = float(diem_tb)
        self.diem_rl = float(diem_rl)
        self.diem_tl = (self.diem_tb + self.diem_rl) / 2

    def to_list(self):
        return [self.ma, self.ho_ten, self.diem_tb, self.diem_rl, self.diem_tl]

def nhap_danh_sach():
    ds = []
    n = int(input("Nhập số sinh viên: "))
    for i in range(n):
        print(f"== Nhập sinh viên thứ {i+1}:")
        ma = input("  Mã SV: ")
        ho_ten = input("  Họ tên: ")
        diem_tb = float(input("  Điểm TB: "))
        diem_rl = float(input("  Điểm RL: "))
        sv = SinhVien(ma, ho_ten, diem_tb, diem_rl)
        ds.append(sv)
    return ds

def ghi_file_csv(ds, ten_file):
    with open(ten_file, mode='w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['Mã SV', 'Họ tên', 'Điểm TB', 'Điểm RL', 'Điểm TL'])
        for sv in ds:
            writer.writerow(sv.to_list())

def sap_xep_theo_diem_rl(ds):
    return sorted(ds, key=lambda sv: sv.diem_rl)

def tim_sv_diem_tl_cao_nhat(ds):
    max_sv = max(ds, key=lambda sv: sv.diem_tl)
    return max_sv