from My_QuanLySinhVien import quanlysinhvien as qlsv
ds_sv = qlsv.nhap_danh_sach()
qlsv.ghi_file_csv(ds_sv, r"bai_tap\My_QuanLySinhVien\ds_sinhvien.py")
ds_sap_xep = qlsv.sap_xep_theo_diem_rl(ds_sv)
print("\n== Danh sách sau khi sắp xếp theo điểm RL tăng dần:")
for sv in ds_sap_xep:
    print(f"{sv.ma} - {sv.ho_ten} - TL: {sv.diem_tl:.2f} - RL: {sv.diem_rl}")

sv_max = qlsv.tim_sv_diem_tl_cao_nhat(ds_sv)
print("\n== Sinh viên có điểm TL cao nhất:")
print(f"{sv_max.ma} - {sv_max.ho_ten} - TL: {sv_max.diem_tl:.2f}")
