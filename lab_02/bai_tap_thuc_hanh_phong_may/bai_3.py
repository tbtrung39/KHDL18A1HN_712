def ten_thu(thu):
    if thu == 1:
        return "Chủ nhật"
    elif thu == 2:
        return "Thứ hai"
    elif thu == 3:
        return "Thứ ba"
    elif thu == 4:
        return "Thứ tư"
    elif thu == 5:
        return "Thứ năm"
    elif thu == 6:
        return "Thứ sáu"
    elif thu == 7:
        return "Thứ bảy"
    else:
        return "Thứ không hợp lệ"

while True:
    thu = int(input("Nhập thứ (1-7): "))
    ten = ten_thu(thu)
    if ten != "Thứ không hợp lệ":
        print(ten)
        break
    else:
        print("Thứ không hợp lệ, vui lòng nhập lại.")