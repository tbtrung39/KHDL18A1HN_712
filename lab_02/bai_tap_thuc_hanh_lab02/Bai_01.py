month = int(input("Nhập tháng (1-12): "))

if month in [1, 3, 5, 7, 8, 10, 12]:
    print("Tháng", month, "có 31 ngày.")
elif month in [4, 6, 9, 11]:
    print("Tháng", month, "có 30 ngày.")
elif month == 2:
    print("Tháng 2 có 28 hoặc 29 ngày.")
else:
    print("Tháng bạn nhập không hợp lệ, vui lòng nhập lại (1-12)")