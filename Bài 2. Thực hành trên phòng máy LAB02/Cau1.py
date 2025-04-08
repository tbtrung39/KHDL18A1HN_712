# Cau 1.
thang = int(input("Nhập tháng (1-12): "))
nam = int(input("Nhập năm: "))
if thang < 1 or thang > 12:
    print("Tháng không hợp lệ!")
else:
    so_ngay_trong_thang = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if thang == 2:
        if (nam % 4 == 0 and nam % 100 != 0) or (nam % 400 == 0):
            ngay = 29
        else:
            ngay = 28
    else:
        ngay = so_ngay_trong_thang[thang - 1]
    print(f"Tháng {thang} năm {nam} có {ngay} ngày.")
