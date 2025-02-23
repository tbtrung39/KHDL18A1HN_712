diem = float(input("Nhập điểm tổng kết: "))
if diem >= 0 and diem <= 3:
    print("Loại Kém")
elif diem > 3 and diem <= 4:
    print("Loại Yếu")
elif diem > 4 and diem <= 5:
    print("Loại Trung bình")
elif diem > 5 and diem <= 7:
    print("Loại Khá")
elif diem > 7 and diem <= 9:
    print("Loại Giỏi")
elif diem > 9 and diem <= 10:
    print("Loại Xuất sắc")
else:
    print("Điểm không hợp lệ!")