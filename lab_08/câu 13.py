def is_leap_year(y):
    """
    Hàm kiểm tra năm y có phải là năm nhuận không.
    Trả về True nếu là năm nhuận, ngược lại False.
    """
    return (y % 400 == 0) or (y % 4 == 0 and y % 100 != 0)

def days_in_month(m, y):
    """
    Hàm trả về số ngày tối đa của tháng m trong năm y.
    Nếu tháng không hợp lệ (không nằm trong khoảng 1-12), trả về -1.
    """
    if m in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    elif m in [4, 6, 9, 11]:
        return 30
    elif m == 2:
        return 29 if is_leap_year(y) else 28
    else:
        return -1

y = int(input("Nhập năm y: "))
m = int(input("Nhập tháng m (1-12): "))

if is_leap_year(y):
    print(f"Năm {y} là năm nhuận.")
else:
    print(f"Năm {y} không phải là năm nhuận.")

so_ngay = days_in_month(m, y)
if so_ngay == -1:
    print("Tháng không hợp lệ!")
else:
    print(f"Tháng {m} năm {y} có {so_ngay} ngày.")
