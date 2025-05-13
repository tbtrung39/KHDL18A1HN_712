import datetime
day = int(input("Nhap ngay: "))
month = int(input("Nhap thang: "))
year = int(input("Nhap nam: "))
date = datetime.date(year, month, day)
week_number = date.isocalendar()[1]

print(f"Ngay {day}/{month}/{year} thuoc tuan thu {week_number} trong nam.")
