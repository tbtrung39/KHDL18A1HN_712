def nhap_sv():
    ho_ten = input("Họ tên: ")
    toan = float(input("Điểm Toán: "))
    ly = float(input("Điểm Lý: "))
    hoa = float(input("Điểm Hóa: "))
    diem_tb = (toan + ly + hoa) / 3
    return ho_ten, diem_tb

ht, tb = nhap_sv()
print(f"{ht} có điểm trung bình: {tb:.2f}")