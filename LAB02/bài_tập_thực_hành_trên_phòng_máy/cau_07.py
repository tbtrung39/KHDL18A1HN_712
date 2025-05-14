diem = float(input("Nhập điểm học sinh:"))
if 0<= diem <=3 :
    print("loại Kém")
elif diem <= 4 :
    print("loại Yếu")
elif diem <= 6 :
    print("loại Trung bình")
elif diem <= 8 :
    print("loại Khá")
elif diem <= 10 :
    print("loại Giỏi")
else :
    print("Điểm không hợp lệ hãy kiểm tra lại!")