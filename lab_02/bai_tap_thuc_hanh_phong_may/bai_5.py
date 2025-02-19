def ten_thang(thang):
    if thang == 1:
        return "Tháng Một"
    elif thang == 2:
        return "Tháng Hai"
    elif thang == 3:
        return "Tháng Ba"
    elif thang == 4:
        return "Tháng Tư"
    elif thang == 5:
        return "Tháng Năm"
    elif thang == 6:
        return "Tháng Sáu"
    elif thang == 7:
        return "Tháng Bảy"
    elif thang == 8:
        return "Tháng Tám"
    elif thang == 9:
        return "Tháng Chín"
    elif thang == 10:
        return "Tháng Mười"
    elif thang == 11:
        return "Tháng Mười Một"
    elif thang == 12:
        return "Tháng Mười Hai"
    else:
        return "Tháng không hợp lệ"

while True:
    thang = int(input("Nhập tháng (1-12): "))
    ten = ten_thang(thang)
    if ten != "Tháng không hợp lệ":
        print(ten)
        break
    else:
        print("Tháng không hợp lệ, vui lòng nhập lại.")