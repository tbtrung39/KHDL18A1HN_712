def kiem_tra_nam_nhuan(nam):
    if (nam % 400 == 0) or (nam % 4 == 0 and nam % 100 != 0):
        return True
    else:
        return False
def so_ngay_trong_thang(thang, nam):
    ngay_cac_thang = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if thang == 2:
        if kiem_tra_nam_nhuan(nam):
            return 29
        else:
            return 28
    elif 1 <= thang <= 12:
        return ngay_cac_thang[thang - 1]
    else:
        return "Tháng không hợp lệ"

nam = int(input("Nhập năm: "))
thang = int(input("Nhập tháng: "))
if kiem_tra_nam_nhuan(nam):
    print(f"Năm {nam} là năm nhuận.")
else:
    print(f"Năm {nam} không phải là năm nhuận.")
so_ngay = so_ngay_trong_thang(thang, nam)
print(f"Tháng {thang} năm {nam} có {so_ngay} ngày.")
