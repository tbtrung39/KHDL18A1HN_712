def nhap_thong_tin():
    ho_ten = input("Nhập họ tên: ")
    toan = float(input("Nhập điểm Toán: "))
    ly = float(input("Nhập điểm Lý: "))
    hoa = float(input("Nhập điểm Hóa: "))
    return ho_ten, toan, ly, hoa

def diem_tb(toan, ly, hoa):
    return (toan + ly + hoa) / 3

def xuat_thong_tin(ho_ten, dtb):
    print(f"{ho_ten} có điểm trung bình là: {dtb:.2f}")

ho_ten, toan, ly, hoa = nhap_thong_tin()
dtb = diem_tb(toan, ly, hoa)
xuat_thong_tin(ho_ten, dtb)
