def nhap_thong_tin():
    ho_ten = input("Nhập họ tên sinh viên: ")
    toan = float(input("Nhập điểm Toán: "))
    ly = float(input("Nhập điểm Lý: "))
    hoa = float(input("Nhập điểm Hóa: "))
    return ho_ten, toan, ly, hoa

def tinh_trung_binh(toan, ly, hoa):
    return (toan + ly + hoa) / 3

def xuat_thong_tin(ho_ten, dtb):
    print(f"Họ tên sinh viên: {ho_ten}")
    print(f"Điểm trung bình: {dtb:.2f}") 

ho_ten, toan, ly, hoa = nhap_thong_tin()
dtb = tinh_trung_binh(toan, ly, hoa)
xuat_thong_tin(ho_ten, dtb)
