from My_QuanLySinhvien import quanlysinhvien

def menu():
    print("\n=== QUẢN LÝ SINH VIÊN ===")
    print("1. Nhập danh sách sinh viên")
    print("2. Tính điểm tích lũy")
    print("3. In danh sách sinh viên")
    print("4. Lưu danh sách vào file CSV")
    print("5. Sắp xếp theo điểm RL")
    print("6. Tìm sinh viên có điểm TL cao nhất")
    print("0. Thoát")

ds_sinh_vien = []
while True:
    menu()
    choice = input("Nhập lựa chọn (0-6): ")
    if choice == '1':
        ds_sinh_vien = quanlysinhvien.nhap_danh_sach_sinh_vien()
    elif choice == '2':
        quanlysinhvien.tinh_diem_tl(ds_sinh_vien)
        print("Đã tính điểm tích lũy cho tất cả sinh viên!")
    elif choice == '3':
        quanlysinhvien.in_danh_sach_sinh_vien(ds_sinh_vien)
    elif choice == '4':
        quanlysinhvien.luu_file_csv(ds_sinh_vien)
    elif choice == '5':
        quanlysinhvien.sap_xep_theo_diem_rl(ds_sinh_vien)
        print("Đã sắp xếp danh sách theo điểm RL!")
        quanlysinhvien.in_danh_sach_sinh_vien(ds_sinh_vien)
    elif choice == '6':
        quanlysinhvien.tim_sinh_vien_diem_tl_cao_nhat(ds_sinh_vien)
    elif choice == '0':
        print("Thoát chương trình!")
        break
    else:
        print("Lựa chọn không hợp lệ!")