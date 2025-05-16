from My_QuanLySinhvien import quanlysinhvien as qlsv

def main():
    # a. Nhập danh sách
    ds = qlsv.nhap_danh_sach()

    # b. Tính điểm TL (đã tính trong lớp)

    # c. Ghi sinh viên yếu ra file
    qlsv.luu_sinhvien_yeu(ds)

    # d. Sắp xếp theo điểm RL tăng dần
    ds_sap_xep = qlsv.sap_xep_theo_rl(ds)
    print("\nDanh sách sắp xếp theo điểm RL:")
    for sv in ds_sap_xep:
        print(sv)

    # e. Sinh viên có TL cao nhất
    print("\nSinh viên có điểm TL cao nhất:")
    for sv in qlsv.tim_sv_tl_cao_nhat(ds):
        print(sv)

if __name__ == "__main__":
    main()
