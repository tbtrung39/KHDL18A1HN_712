diem = float(input("Nhập điểm tổng kết: "))
if diem < 0 or diem > 10:
    print("Điểm không hợp lệ, vui lòng nhập lại!")
elif diem >= 0 and diem < 3.0:
    print("Loại Kém")
elif diem == 4.0:
    print("Loại Yếu")
elif diem >= 5.0 and diem < 6.0:
    print("Loại Trung bình")
elif diem >= 7.0 and diem < 8.0:
    print("Loại Khá")
elif diem >= 9.0 and diem <= 10.0:
    print("Loại Giỏi")
