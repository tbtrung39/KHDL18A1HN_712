def nhap_sinh_vien():
    ho_ten = input("Nhập họ tên sinh viên: ")
    diem_toan = float(input("Nhập điểm Toán: "))
    diem_ly = float(input("Nhập điểm Lý: "))
    diem_hoa = float(input("Nhập điểm Hóa: "))
    return ho_ten, diem_toan, diem_ly, diem_hoa
def tinh_diem_trung_binh(diem_toan, diem_ly, diem_hoa):
    return (diem_toan + diem_ly + diem_hoa) / 3
def xuat_sinh_vien(ho_ten, diem_toan, diem_ly, diem_hoa, diem_tb):
    print(f"Họ tên: {ho_ten}")
    print(f"Điểm Toán: {diem_toan}")
    print(f"Điểm Lý: {diem_ly}")
    print(f"Điểm Hóa: {diem_hoa}")
    print(f"Điểm trung bình: {diem_tb:.2f}")
ho_ten, dt, dl, dh = nhap_sinh_vien()
diem_tb = tinh_diem_trung_binh(dt, dl, dh)
xuat_sinh_vien(ho_ten, dt, dl, dh, diem_tb)
