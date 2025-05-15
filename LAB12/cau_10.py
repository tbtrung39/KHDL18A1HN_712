from datetime import datetime

try:
    d1 = datetime.strptime(input("Ngay 1 (dd-mm-yyyy): "), '%d-%m-%Y')
    d2 = datetime.strptime(input("Ngay 2 (dd-mm-yyyy): "), '%d-%m-%Y')

    if d1 > d2:
        d1, d2 = d2, d1


    delta_days = (d2 - d1).days

    years = delta_days // 365
    remaining_days = delta_days % 365
    months = remaining_days // 30
    days = remaining_days % 30

    print(f"Cách nhau: {years} năm, {months} tháng, {days} ngày")

except ValueError:
    print("Lỗi: Ngày nhập vào không đúng định dạng!")