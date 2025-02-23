ngay = int(input("Nhập ngày: "))
thang =int(input("Nhập tháng: "))
if thang==1 or thang==3 or thang==5 or thang==7 or thang==8 or thang==10 or thang==12 :
    so_ngay_trong_thang = 31
elif thang==4 or thang==6 or thang==9 or thang==11:
    so_ngay_trong_thang = 30
else:
    so_ngay_trong_thang = 28
if ngay <1 or ngay> so_ngay_trong_thang :
    print("Ngày không hợp lệ. Vui lòng nhập lại")
else:
    if ngay < so_ngay_trong_thang :
        ngay +=1
    else:
        ngay = 1
        if thang ==12:
            thang=1
        else:
            thang+=1
    print("Ngày tiếp theo là: ", ngay,"/",thang)