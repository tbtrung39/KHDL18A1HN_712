ngay = int(input("Nhập ngày: "))
thang = int(input("Nhập tháng: "))

if 1 <= thang <= 12:
    if 1 <= ngay <= 31:
        if thang == 2:
            songaytoida = 28
        elif thang in [4, 6, 9, 11]:
            songaytoida = 30
        else:
            songaytoida = 31

        if ngay < songaytoida:
            ngay += 1
        else:
            ngay = 1
            if thang < 12:
                thang += 1
            else:
                thang = 1

        print("Ngày tiếp theo là:", ngay, "/", thang)
    else:
        print("Ngày không đúng định dạng, vui lòng nhập lại")
else:
    print("Tháng không đúng định dạng, vui lòng nhập lại")
