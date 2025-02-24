print("Chương trình xác định số ngày trong một tháng")
tg = int(input("Nhập tháng: "))
if 1 <= tg <= 12 :
    if tg == 1 :
        print("Tháng 1 có 31 ngày")
    elif tg == 2 :
        print("Tháng 2 năm nhuận có 29 ngày , Tháng 2 năm không nhuận có 28 ngày")
    elif tg == 3 :
        print("Tháng 3 có 31 ngày")
    elif tg == 4 :
        print("Tháng 4 có 30 ngày")
    elif tg == 5 :
        print("Tháng 5 có 31 ngày")
    elif tg == 6 :
        print("Tháng 6 có 30 ngày")
    elif tg == 7 :
        print("Tháng 7 có 31 ngày")
    elif tg == 8 :
        print("Tháng 8 có 31 ngày")
    elif tg == 9 :
        print("Tháng 9 có 30 ngày")
    elif tg == 10 :
        print("Tháng 10 có 31 ngày")
    elif tg == 11 :
        print("Tháng 11 có 30 ngày")
    elif tg == 12 :
        print("Tháng 12 có 31 ngày")
else : 
    print("Vui lòng nhập lại")