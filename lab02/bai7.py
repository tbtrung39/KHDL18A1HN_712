hoc_luc = float(input("Nhập học lực của học sinh : "))
if hoc_luc >= 0 and hoc_luc < 4 : 
    print("Loại Kém")
elif hoc_luc <5 : 
    print("Loại YếuYếu")
elif hoc_luc < 7  : 
    print("Loại Trung bình")
elif hoc_luc < 9 :
    print("Loại khá")
elif hoc_luc <= 10 : 
    print("Loại giỏi")