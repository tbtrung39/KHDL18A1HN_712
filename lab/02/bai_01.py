năm = int(input("Nhập năm :"))
tháng = int(input("Nhập tháng:"))
if (năm %4 == 0 and năm%100!=0 or năm%400==0) and tháng == 2:
    print("tháng 2 có 29 ngày")
elif (năm%4!= 0 or năm%100==0 or năm%400!=0) and tháng ==2:
    print("tháng 2 có 28 ngày")
elif (tháng==1 or tháng==3 or tháng==5 or tháng==7 or tháng==8 or tháng==10 or tháng==12):
    print("tháng", tháng, "có 31 ngày")
elif (tháng==4 or tháng==6 or tháng==9 or tháng ==11):
    print("tháng",tháng, "có 30 ngày")
else:
    print("không hợp lệ . Vui lòng nhập lại")