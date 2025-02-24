def ngay_tiep_theo(ngay, thang, nam):
    ngay_trong_thang = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30,
                        7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
    if (nam % 4 == 0 and nam % 100 != 0) or (nam % 400 == 0):
        ngay_trong_thang[2] = 29
    if ngay < ngay_trong_thang[thang]:
        ngay += 1
    else:
        ngay = 1
        if thang == 12:
            thang = 1
            nam += 1
        else:
            thang += 1
    return f"Ngày tiếp theo là ngày {ngay}/{thang}/{nam}"

ngay = int(input("Nhập ngày: "))
thang = int(input("Nhập tháng: "))
nam = int(input("Nhập năm: "))
print(ngay_tiep_theo(ngay, thang, nam))
