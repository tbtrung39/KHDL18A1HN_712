ngay=int(input("Nhap ngay"))
thang=int(input("Nhap thap"))
if thang >= 1 and thang <=12:
    if ngay>=1 and ngay<=31:
        if thang==2:
            songaytoida=28
        elif thang ==4 or thang==6 or thang==9 or thang ==11:
            songaytoida=30
        else:
            songaytoida=31
        if ngay<songaytoida:
            ngay=ngay+1
        else:
            ngay=1
            if thang<12:
                thang+=1
            else:
                thang=1
        print("ngay tiep theo la:",ngay,"/",thang)
    else:
        print("Ngay khong dung dinh dang ,vui long nhap lai")
else:
    print("thang khong dung dinh dang,vui long nhap lai")
