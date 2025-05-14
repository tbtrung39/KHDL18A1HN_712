import quanlysinhvien as qlsv

def menu():
    ds = qlsv.doc_file()

    while True:
        print("\n--- MENU ---")
        print("1. Nhập danh sách sinh viên")
        print("2. Tính điểm TL")
        print("3. In danh sách")
        print("4. Sắp xếp theo RL tăng dần")
        print("5. In sinh viên có TL cao nhất")
        print("0. Thoát")

        chon = input("Chọn: ")
        if chon == '1':
            ds = qlsv.nhap_danh_sach()
            qlsv.ghi_file(ds)
        elif chon == '2':
            # TL đã tính lúc nhập rồi
            print("Điểm TL đã được tính khi nhập!")
        elif chon == '3':
            qlsv.in_danh_sach(ds)
        elif chon == '4':
            ds = qlsv.sap_xep_theo_rl(ds)
            qlsv.in_danh_sach(ds)
        elif chon == '5':
            top = qlsv.sv_tl_cao_nhat(ds)
            qlsv.in_danh_sach(top)
        elif chon == '0':
            break
        else:
            print("Lựa chọn không hợp lệ!")

menu()
