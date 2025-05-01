def kiem_tra_nam_nhuan(nam):
    if (nam % 400 == 0) or (nam % 4 == 0 and nam % 100 != 0):
        return True
    else:
        return False

def so_ngay_trong_thang(thang, nam):
    if thang in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    elif thang in [4, 6, 9, 11]:
        return 30
    elif thang == 2:
        if kiem_tra_nam_nhuan(nam):
            return 29
        else:
            return 28
    else:
        return "Tháng không hợp lệ!"

nam = int(input("Nhập năm: "))
thang = int(input("Nhập tháng: "))

if kiem_tra_nam_nhuan(nam):
    print(f"Năm {nam} là năm nhuận.")
else:
    print(f"Năm {nam} không phải là năm nhuận.")

so_ngay = so_ngay_trong_thang(thang, nam)
print(f"Tháng {thang} năm {nam} có {so_ngay} ngày.")
