def is_leap_year(year):
    return (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0)
def days_in_month(month, year):
    if month in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    elif month in [4, 6, 9, 11]:
        return 30
    elif month == 2:
        return 29 if is_leap_year(year) else 28
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