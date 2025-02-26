diem_tk =float(input("Nhập điểm tổng kết của học sinh: "))
if 0.0 <= diem_tk <= 3.0 :
    print("loại kém")
elif diem_tk ==4 :
    print("loại yếu")
elif 5.0 <= diem_tk <= 6.0 :
    print("loại trung bình")
elif 7.0 <= diem_tk <=8.0 :
    print("loại khá")
elif 9.0 <= diem_tk <= 10.0 :
    print("loại giỏi")
else:
    print("Diểm không hợp lệ .Vui lòng nhập lại")