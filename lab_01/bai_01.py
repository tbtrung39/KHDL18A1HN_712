def nhap_sinh_vien():
    ma_sv = input("Nhập mã số sinh viên: ")
    ho_ten = input("Nhập họ và tên: ")
    que_quan = input("Nhập quê quán: ")
    nam_sinh = int(input("Nhập năm sinh: "))
    diem_tb = float(input("Nhập điểm trung bình: "))

    print("\nThông tin sinh viên:")
    print(f"Mã SV: {ma_sv}")
    print(f"Họ tên: {ho_ten}")
    print(f"Quê quán: {que_quan}")
    print(f"Năm sinh: {nam_sinh}")
    print(f"Điểm trung bình: {diem_tb:.2f}")

nhap_sinh_vien()
