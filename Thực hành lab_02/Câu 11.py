#Câu 11:
ngay = int(input("Nhập ngày: "))
thang = int(input("Nhập tháng: "))
if ( thang ==1 or thang == 3 or thang == 5 or thang == 7 or thang == 7 or thang == 8 or thang == 10 or thang == 12):
    if ngay<31:
        ngay+=1
        print("ngày",ngay,"tháng",thang)
    elif ngay ==31:
        if thang!=12:
            thang+=1
            print("ngày 1 tháng",thang)
        elif thang == 12: 
            print("ngày 1 tháng 1")
    else:
        print("ngày không hợp lệ hãy nhập lại")
elif thang == 2:
    if ngay < 28 :
        ngay+=1
        print("ngày",ngay,"tháng 2")
    elif ngay == 28:
        print("ngày 1 tháng 3")
    else: print("ngày không hợp lệ hãy nhập lại")
elif thang == 4 or thang==6 or thang == 9 or thang == 11 :
    if ngay < 30 :
        ngay += 1
        print("ngày",ngay,"tháng",thang)
    elif ngay == 30 :
        thang+=1
        print("ngày 1 tháng",thang)
    else:
        print("ngày không hợp lệ hãy nhập lại")
else:
    print("tháng không hợp lệ hãy nhập lại")