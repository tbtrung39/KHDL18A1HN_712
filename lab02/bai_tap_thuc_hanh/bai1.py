thang = int(input("Nhập vào tháng (1-12): "))
if thang in [1, 3, 5, 7, 8, 10, 12]:
    print("Tháng", thang, "có 31 ngày")
elif thang in [4, 6, 9, 11]:
    print("Tháng", thang, "có 30 ngày")
elif thang == 2:
    print("Tháng 2 có 28 hoặc 29 ngày")
else:
    print("Tháng không hợp lệ")