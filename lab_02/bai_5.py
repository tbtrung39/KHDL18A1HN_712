print("Chương trình xác định tên tháng")
tg = int(input("Nhập tháng: "))
if 1 <= tg <= 12:
    if tg == 1:
        print("January")
    elif tg == 2:
        print("February")
    elif tg == 3:
        print("March")
    elif tg == 4:
        print("April")
    elif tg == 5:
        print("May")
    elif tg == 6:
        print("June")
    elif tg == 7:
        print("July")
    elif tg == 8:
        print("August")
    elif tg == 9:
        print("September")
    elif tg == 10:
        print("October")
    elif tg == 11:
        print("November")
    elif tg == 12:
        print("December")
else:
    print("Vui lòng nhập lại")
