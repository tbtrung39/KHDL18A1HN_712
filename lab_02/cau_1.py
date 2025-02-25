n=int(input("nhap thang can tra:"))
if n>=1 and n<=12:
    if n==1 or n==3 or n==5 or n==7 or n==8 or n==10 or n==12:
        print("thang",n,"co 31 ngay")
    elif n==2 :
        print("thang 2 co 28 ngay")
    else:
        print("thang",n,"co 30 ngay")
else:print("nhap sai. vui long nhap lai")