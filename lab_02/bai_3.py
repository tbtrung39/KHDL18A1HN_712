print("Chương trình xác định tên thứ trong tuần")
t = int(input("Nhập số thứ trong tuần: "))
if 1 <= t <= 7:
    if t == 1:
        print("Sunday")
    elif t == 2:
        print("Monday")
    elif t == 3:
        print("Tuesday")
    elif t == 4:
        print("Wednesday")
    elif t == 5:
        print("Thursday")
    elif t == 6:
        print("Friday")
    elif t == 7:
        print("Saturday")
else:
    print("Vui lòng nhập lại")
