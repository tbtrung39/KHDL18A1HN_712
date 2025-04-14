def la_nam_nhuan(nam):
    return nam % 4 == 0 and (nam % 100 != 0 or nam % 400 == 0)

def ngay_toi_da(thang, nam):
    if thang in [1, 3, 5, 7, 8, 10, 12]: return 31
    elif thang in [4, 6, 9, 11]: return 30
    elif thang == 2: return 29 if la_nam_nhuan(nam) else 28
    return "Tháng không hợp lệ"

thang = int(input("Nhập tháng: "))
nam = int(input("Nhập năm: "))
print(f"Số ngày tối đa trong tháng {thang}/{nam}: {ngay_toi_da(thang, nam)}")