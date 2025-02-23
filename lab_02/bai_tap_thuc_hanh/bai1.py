thang = int(input("Nhap thang (1-12): "))
if thang == 1 or thang == 3 or thang == 5 or thang == 7 or thang == 8 or thang == 10 or thang == 12:
    print("Thang", thang, "co 31 ngay .")
elif thang == 4 or thang == 6 or thang == 9 or thang == 11:
    print("Thang", thang, "co 30 ngay.")
elif thang == 2:
    print("Thang 2 co 28 ngay.")
else:
    print("Thang khong hop le. Vui long nhap lai")