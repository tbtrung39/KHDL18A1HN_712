thang=int(input("Nhập số tháng: "))
ngay=int(input("nhap so ngay: "))
if thang >=1 and thang<=12:
    if thang ==1 or thang==3 or thang ==5 or thang == 7 or thang == 8 or thang ==10 or thang ==12 and ngay<=31:
        if ngay<31:
            print("ngay tiep theo 1 ngay la: ngay",ngay+1,"thang",thang)
        else:
            print("ngay tiep theo 1 ngay la: ngay 1 thang",thang+1)
    elif thang ==2 and ngay <=28:
        if ngay<28:
            print("ngay tiep theo 1 ngay la: ngay",ngay+1,"thang",thang)
        else:
            print("ngay tiep theo 1 ngay la: ngay 1 thang",thang+1)
    else:
        if ngay<30:
            print("ngay tiep theo 1 ngay la: ngay",ngay+1,"thang",thang)
        else:
            print("ngay tiep theo 1 ngay la: ngay 1 thang",thang+1)
else:
    print("so thang khong hop li. Vui long nhap lai")