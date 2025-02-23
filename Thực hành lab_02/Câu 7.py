#Câu 7:
diem = float(input("Nhập điểm tổng kết của học sinh"))
if 0<= diem <=3:
    print("loại kém")
elif diem == 4 :
    print("Loại yếu")
elif diem <= 6 :
    print("loại trung bình")
elif diem <= 8 :
    print("loại khá")
elif diem <= 10 :
    print("loại giỏi")
else:
    print("điểm không hợp lệ hãy kiểm tra lại")