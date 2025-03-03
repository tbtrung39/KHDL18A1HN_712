def so_ngay_trong_thang(thang):
    if thang in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    elif thang == 2:
        return 28
    elif thang in [4, 6, 9, 11]:
        return 30
    else:
        return "Tháng không hợp lệ"