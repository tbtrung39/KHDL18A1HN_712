def nhap_thong_tin_sinh_vien():
    """Nhập thông tin sinh viên."""
    ma_sv = input("Mã số sinh viên: ")
    ho_ten = input("Họ tên: ")
    que_quan = input("Quê quán: ")
    nam_sinh = int(input("Năm sinh: "))
    diem_tb = float(input("Điểm trung bình: "))
    return ma_sv, ho_ten, que_quan, nam_sinh, diem_tb

def xuat_thong_tin_sinh_vien(ma_sv, ho_ten, que_quan, nam_sinh, diem_tb):
    """Xuất thông tin sinh viên."""
    print("\nThông tin sinh viên:")
    print(f"Mã số: {ma_sv}")
    print(f"Họ tên: {ho_ten}")
    print(f"Quê quán: {que_quan}")
    print(f"Năm sinh: {nam_sinh}")
    print(f"Điểm TB: {diem_tb}")

# Sử dụng
ma_sv, ho_ten, que_quan, nam_sinh, diem_tb = nhap_thong_tin_sinh_vien()
xuat_thong_tin_sinh_vien(ma_sv, ho_ten, que_quan, nam_sinh, diem_tb)