ngay = int(input("Nhập ngày: "))
thang = int(input("Nhập tháng: "))

if 1 <= thang <= 12:
    ngay_max = 31
    if thang in [4, 6, 9, 11]:
        ngay_max = 30
    elif thang == 2:
        ngay_max = 28
    
    if 1 <= ngay <= ngay_max:
        ngay += 1
        if ngay > ngay_max:
            ngay = 1
            thang += 1
            if thang > 12:
                thang = 1  # Chuyển sang năm mới
        print("Ngày tiếp theo là:", ngay, "/", thang)
    else:
        print("Ngày không hợp lệ")
else:
    print("Tháng không hợp lệ")