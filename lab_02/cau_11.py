thang=int(input("Nhập số tháng: "))
if thang >=1 and thang<=12:
    if thang ==1 or thang==3 or thang ==5 or thang == 7 or thang == 8 or thang ==10 or thang ==12:
        print("thang",thang,"co 31 ngay")
    elif thang ==2:
        print("thang 2 co 28 ngay vao nam khong nhuan hoac 29 ngay vao nam nhuan")
    else:
        print("thang",thang,"co 30 ngay")
else:
    print("so thang khong hop li. Vui long nhap lai")