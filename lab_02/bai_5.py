def ten_thang_trong_nam(thang):
    thang_dict = {
        1: "Tháng Một", 2: "Tháng Hai", 3: "Tháng Ba", 4: "Tháng Tư",
        5: "Tháng Năm", 6: "Tháng Sáu", 7: "Tháng Bảy", 8: "Tháng Tám",
        9: "Tháng Chín", 10: "Tháng Mười", 11: "Tháng Mười Một", 12: "Tháng Mười Hai"
    }
    if 1 <= thang <= 12:
        return thang_dict[thang]
    else:
        return "Tháng không hợp lệ"