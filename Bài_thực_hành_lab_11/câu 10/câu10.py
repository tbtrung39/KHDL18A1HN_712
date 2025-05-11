from My_QuanLySinhvien.quanlysinhvien import QuanLySinhVien

def main():
    qlsv = QuanLySinhVien()
    
    while True:
        print("\nCHƯƠNG TRÌNH QUẢN LÝ SINH VIÊN")
        print("1. Nhập danh sách sinh viên")
        print("2. Hiển thị danh sách sinh viên")
        print("3. Lưu danh sách vào file CSV")
        print("4. Sắp xếp theo điểm rèn luyện")
        print("5. Tìm sinh viên có điểm tích lũy cao nhất")
        print("0. Thoát")
        
        choice = input("Chọn chức năng (0-5): ")
        
        if choice == '1':
            qlsv.nhap_sinh_vien()
        elif choice == '2':
            qlsv.in_danh_sach()
        elif choice == '3':
            qlsv.luu_file_csv()
        elif choice == '4':
            qlsv.sap_xep_theo_diem_rl()
            qlsv.in_danh_sach()
        elif choice == '5':
            qlsv.tim_sv_diem_tl_cao_nhat()
        elif choice == '0':
            print("Kết thúc chương trình!")
            break
        else:
            print("Lựa chọn không hợp lệ. Vui lòng chọn lại!")

main()