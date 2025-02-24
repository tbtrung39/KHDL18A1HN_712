nam=int(input("Nhập năm:"))
thang=int(input("Nhập tháng:"))
if (nam%4!=0 and nam%100!=0 or nam%400==0) and thang == 2 :
    print("tháng 2 có 29 ngày")
elif (nam%4!=0 and nam%100!=0 or nam%400==0) and thang == 2 :
    print("tháng 2 có 28 ngày")

if (thang==1 or thang==3 or thang ==5 or thang==7 or thang==8 or thang==10 or thang==12) :
    print("tháng",thang,"có 31 ngày")
elif thang==4 or thang==6 or thang==9 or  thang==11:
    print("tháng",thang,"có 30 ngày")
else:
    print("tháng không hợp lệ vui lòng nhập lại")