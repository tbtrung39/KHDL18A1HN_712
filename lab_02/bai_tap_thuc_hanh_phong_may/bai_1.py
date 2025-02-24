def so_ngay_trong_thang(thang, nam):
    if thang in (1, 3, 5, 7, 8, 10, 12):
        return 31
    elif thang in (4, 6, 9, 11):
        return 30
    elif thang == 2:
        return 29 if (nam % 4 == 0 and nam % 100 != 0) or (nam % 400 == 0) else 28
    else:
        return "Tháng không hợp lệ"

thang = int(input("Nhập vào tháng: "))
nam = int(input("Nhập vào năm: "))
print(f"Tháng {thang} năm {nam} có {so_ngay_trong_thang(thang, nam)} ngày.")
