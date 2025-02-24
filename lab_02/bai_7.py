print("Chương trình xếp loại học lực")
diem = float(input("Nhập điểm tổng kết: "))
if 0 <= diem <= 3:
    print("Loại Kém")
elif diem == 4:
    print("Loại Yếu")
elif 5 <= diem <= 6:
    print("Loại Trung bình")
elif 7 <= diem <= 8:
    print("Loại Khá")
elif 9 <= diem <= 10:
    print("Loại Giỏi")
else:
    print("Vui lòng nhập lại")