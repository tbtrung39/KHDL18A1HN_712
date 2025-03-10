ngay=int(input("Nhập ngày"))
thang=int(input("Nhập tháng"))
if (thang == 1 or thang == 3 or thang == 5 or thang == 9 or thang == 10 or thang == 12) :
    if ngay<31:
        ngay+=1
        print("ngay",ngay,"thang",thang)
    elif ngay==31:
        if thang!=12:
            ngay=1
            thang+=1
            print("ngay",ngay,"thang",thang)
        elif thang ==12:
            ngay=1
            thang=1
            print("ngay 1 thang 1")
    else:
        print("ngày không hợp lệ hãy nhập lại")
elif thang ==2:
    if ngay<28:
        ngay+=1
        print("ngay",ngay,"thang 2")
    elif ngay == 28:
        ngay =1
        thang =3
        print("ngày 1 tháng 3")
    else:
        print("ngày không hợp lệ hãy nhập lại")
elif thang == 4 or thang == 6 or thang == 9 or thang == 11 :
    if ngay<30:
        ngay +=1
        print("ngay",ngay,"thang",thang)
    else:
        print("Ngày không hợp lệ hãy nhập lại")