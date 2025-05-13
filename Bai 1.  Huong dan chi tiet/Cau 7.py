# Cau 7.

def is_leap(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)
def day_of_year(date):
    year, month, day = date[2], date[1], date[0]
    days_in_month = [31, 28 + is_leap(year), 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if year < 1:
        raise ValueError("Nam khong hop le")
    if not 1 <= month <= 12:
        raise ValueError("Thang khong hop le")
    if not 1 <= day <= days_in_month[month - 1]:
        raise ValueError("Ngay khong hop le")
    return sum(days_in_month[:month - 1]) + day + (1 if is_leap(year) and month > 2 else 0)
try:
    day = int(input("Nhap ngay: "))
    month = int(input("Nhap thang: "))
    year = int(input("Nhap nam: "))
    date = (day, month, year)
    day_number = day_of_year(date)
    print("Ngay {} thang {} nam {} la ngay thu {} trong nam.".format(day, month, year, day_number))
except ValueError as e:
    print("Loi:", e)
