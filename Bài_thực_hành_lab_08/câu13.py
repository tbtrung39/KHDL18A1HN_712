def nam_nhuan(y):
    return (y % 4 == 0 and y % 100 != 0) or (y % 400 == 0)

def so_ngay_thang(m, y):
    if m in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    elif m in [4, 6, 9, 11]:
        return 30
    elif m == 2:
        return 29 if nam_nhuan(y) else 28
    else:
        return "Tháng không hợp lệ"

y = int(input("Nhập năm: "))
m = int(input("Nhập tháng: "))

if nam_nhuan(y):
    print(f"Năm {y} là năm nhuận")
else:
    print(f"Năm {y} không phải là năm nhuận")

print(f"Số ngày của tháng {m} năm {y} là: {so_ngay_thang(m, y)}")
