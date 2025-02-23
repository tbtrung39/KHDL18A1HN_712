ngay = int(input("Nhập ngày: "))
thang = int(input("Nhập tháng: "))

if thang == 1 or thang == 3 or thang == 5 or thang == 7 or thang == 8 or thang == 10 or thang == 12:
    so_ngay = 31
elif thang == 4 or thang == 6 or thang == 9 or thang == 11:
    so_ngay = 30
elif thang == 2:
    so_ngay = 28
else:
    so_ngay = 0  # Tháng không hợp lệ

if ngay >= 1 and ngay < so_ngay:
    ngay_tiep_theo = ngay + 1
    thang_tiep_theo = thang
elif ngay == so_ngay:
    ngay_tiep_theo = 1
    if thang == 12:
        thang_tiep_theo = 1
    else:
        thang_tiep_theo = thang + 1
else:
    ngay_tiep_theo = 0
    thang_tiep_theo = 0

if ngay_tiep_theo == 0:
    print("Ngày không hợp lệ!")
else:
    print("Ngày tiếp theo là:", ngay_tiep_theo, "/", thang_tiep_theo)