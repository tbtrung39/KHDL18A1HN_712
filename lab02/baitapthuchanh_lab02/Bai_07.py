diem = float(input("Nhập điểm: "))

if 0.0 <= diem <= 10.0:
    if diem >= 9.0:
        print("Học sinh đạt học lực giỏi")
    elif diem >= 7.0:
        print("Học sinh đạt học lực khá")
    elif diem >= 5.0:
        print("Học sinh đạt học lực trung bình")
    elif diem >= 3.0:
        print("Học sinh đạt học lực yếu")
    else:
        print("Học sinh đạt học lực kém")
else:
    print("Dữ liệu điểm sai, vui lòng nhập lại (0->10)")
