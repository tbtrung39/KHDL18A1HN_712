#Câu 11:
def tinh_trung_binh(toan, ly, hoa):
    return (toan + ly + hoa) / 3
def xuat_thong_tin(ten, tb):
    print("Họ ten: ", ten)
    print("Điểm trung bình: ", round(tb,2))
ten = input("Nhập họ tên sinh viên: ")
toan = float(input("Nhập điểm toán: "))
ly = float(input("Nhập điểm lý: "))
hoa = float(input("Nhập điểm hóa: "))
tb = tinh_trung_binh(toan, ly, hoa)
xuat_thong_tin(ten, tb)