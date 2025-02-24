thang = int(input("Nhập tháng (1-12): "))
nam = int(input("Nhập năm: "))
ngay_trong_thang = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
if thang == 2:
    if (nam % 4 == 0 and nam % 100 != 0) or (nam % 400 == 0):
        result = 29  
    else:
        result = 28 
else:
    result = ngay_trong_thang[thang - 1]
print(f"Tháng {thang} năm {nam} có {result} ngày.")
