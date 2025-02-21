score = float(input("Nhập điểm tổng kết: "))
if 0 <= score <= 3:
    print("Loại Kém")
elif score == 4:
    print("Loại Yếu")
elif 5 <= score <= 6:
    print("Loại Trung bình")
elif 7 <= score <= 8:
    print("Loại Khá")
elif 9 <= score <= 10:
    print("Loại Giỏi")
else:
    print("Điểm không hợp lệ!")