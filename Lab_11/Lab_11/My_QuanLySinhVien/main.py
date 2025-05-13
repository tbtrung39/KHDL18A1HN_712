from quanlysinhvien import *

def hien_thi_danh_sach(danh_sach):
    print(f"{'Mã SV':<10} {'Họ tên':<25} {'TB':<6} {'RL':<6} {'TL':<6}")
    for sv in danh_sach:
        print(f"{sv.ma:<10} {sv.ho_ten:<25} {sv.diem_tb:<6.2f} {sv.diem_rl:<6.2f} {sv.diem_tl:<6.2f}")


def main():
    print("=== NHẬP DANH SÁCH SINH VIÊN ===")
    ds = nhap_danh_sach_sv()

    print("\n=== DANH SÁCH SINH VIÊN VỪA NHẬP ===")
    hien_thi_danh_sach(ds)

    print("\n=== DANH SÁCH ĐÃ SẮP XẾP THEO ĐIỂM RÈN LUYỆN TĂNG DẦN ===")
    ds_sap_xep = sap_xep_theo_rl(ds)
    hien_thi_danh_sach(ds_sap_xep)

    print("\n=== SINH VIÊN CÓ ĐIỂM TÍCH LŨY CAO NHẤT ===")
    sv_max = tim_max_tl(ds)
    hien_thi_danh_sach([sv_max])

    print("\n=== GHI FILE CSV ===")
    ghi_file_csv(ds)
    print("Đã ghi vào file files/ds_sinhvien.csv")


if __name__ == "__main__":
    main()
