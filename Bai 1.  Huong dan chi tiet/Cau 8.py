# Cau 8.

import datetime
def is_leap(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)
def day_of_week(date):
    day, month, year = date[0], date[1], date[2]
    days_in_month = [31, 28 + is_leap(year), 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]   
    if year < 1:
        raise ValueError("Nam khong hop le!")
    if not 1 <= month <= 12:
        raise ValueError("Thang khong hop le!")
    if not 1 <= day <= days_in_month[month - 1]:
        raise ValueError("Ngay khong hop le!")
    if month == 2 and day > 29:
        raise ValueError("Thang 2 khong co ngay {}".format(day))
    if month in [4, 6, 9, 11] and day > 30:
        raise ValueError("Thang {} khong co ngay {}".format(month, day))
    date = datetime.date(year, month, day)
    weekday = date.weekday()
    days_of_week = ['Thu hai', 'Thu ba', 'Thu tu', 'Thu nam', 'Thu sau', 'Thu bay', 'Chu nhat']
    return days_of_week[weekday]
try:
    day = int(input("Nhap ngay: "))
    month = int(input("Nhap thang: "))
    year = int(input("Nhap nam: "))
    date = (day, month, year)
    print(day_of_week(date))
except ValueError as e:
    print(e)
