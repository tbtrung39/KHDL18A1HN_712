def nhap_thong_tin():
    ten = input("Nhập họ tên sinh viên: ")
    toan = float(input("Nhập điểm Toán: "))
    ly = float(input("Nhập điểm Lý: "))
    hoa = float(input("Nhập điểm Hóa: "))
    return ten, toan, ly, hoa

def tinh_trung_binh(toan, ly, hoa):
    return (toan + ly + hoa) / 3

def xuat_thong_tin(ten, tb):
    print(f"Sinh viên {ten} có điểm trung bình: {tb:.2f}")

ten, toan, ly, hoa = nhap_thong_tin()
tb = tinh_trung_binh(toan, ly, hoa)
xuat_thong_tin(ten, tb)
