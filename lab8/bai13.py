def la_nam_nhuan(nam):
    return (nam % 4 == 0 and nam % 100 != 0) or (nam % 400 == 0)

def so_ngay_trong_thang(thang, nam):
    if thang in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    elif thang in [4, 6, 9, 11]:
        return 30
    elif thang == 2:
        return 29 if la_nam_nhuan(nam) else 28
    else:
        return "Tháng không hợp lệ"

nam = int(input("Nhập năm: "))
thang = int(input("Nhập tháng: "))
print(f"Năm {nam} là năm nhuận." if la_nam_nhuan(nam) else f"Năm {nam} không phải năm nhuận.")
print(f"Số ngày trong tháng {thang} năm {nam} là:", so_ngay_trong_thang(thang, nam))
