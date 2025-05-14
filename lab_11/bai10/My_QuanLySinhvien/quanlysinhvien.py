import csv

def SinhVien(ma_sv, ho_ten, diem_tb, diem_rl):
    ma_sv = ma_sv
    ho_ten = ho_ten
    diem_tb = float(diem_tb)
    diem_rl = float(diem_rl)
    tich_luy = (diem_tb + diem_rl) / 2
    return [ma_sv, ho_ten, diem_tb, diem_rl, tich_luy]

def nhap_danh_sach():
    danh_sach = []
    n = int(input("Nhap so luong sinh vien: "))
    for i in range(n):
        print(f"\nSinh vien {i+1}:")
        ma_sv = input("  Ma SV: ")
        ho_ten = input("  Ho ten: ")
        diem_tb = float(input("  Diem TB: "))
        diem_rl = float(input("  Diem RL: "))
        sv = SinhVien(ma_sv, ho_ten, diem_tb, diem_rl)
        danh_sach.append(sv)
    return danh_sach


def ghi_file_csv(danh_sach, ten_file="Bai_2_Thuc_hanh_phong_may\Cau 10\ds_sinhvien.csv"):
    with open(ten_file, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(["Ma SV", "Ho ten", "Diem TB", "Diem RL", "Diem TL"])
        for sv in danh_sach:
            writer.writerow(sv.to_list())


def sap_xep_theo_rl(danh_sach):
    return sorted(danh_sach, key=lambda sv: sv.diem_rl)


def tim_sv_tl_cao_nhat(danh_sach):
    return max(danh_sach, key=lambda sv: sv.tich_luy)
