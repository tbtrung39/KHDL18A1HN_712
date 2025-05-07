from My_QuanLySinhvien import quanlysinhvien as qlsv

def main():
    danh_sach = qlsv.nhap_danh_sach()
    print("\n=== DANH SACH DAY DU ===")
    for sv in danh_sach:
        print(sv.to_list())

    qlsv.ghi_file_csv(danh_sach)
    print("Da luu danh sach vao ds_sinhvien.csv")

    danh_sach_sap_xep = qlsv.sap_xep_theo_rl(danh_sach)
    print("\n=== DANH SACH SAP XEP THEO RL TANG DAN ===")
    for sv in danh_sach_sap_xep:
        print(sv.to_list())

    sv_max = qlsv.tim_sv_tl_cao_nhat(danh_sach)
    print("\n=== SINH VIEN CO DIEM TL CAO NHAT ===")
    print(sv_max.to_list())

if __name__ == "__main__":
    main()
