from datetime import datetime
from dateutil.relativedelta import relativedelta  # Cần cài thư viện: pip install python-dateutil

try:
    date1 = datetime.strptime(input("Nhập ngày thứ nhất (dd-mm-yyyy): "), "%d-%m-%Y")
    date2 = datetime.strptime(input("Nhập ngày thứ hai (dd-mm-yyyy): "), "%d-%m-%Y")

    if date2 < date1:
        date1, date2 = date2, date1  # Đảm bảo date1 < date2

    diff = relativedelta(date2, date1)
    print(f"Khoảng cách: {diff.years} năm, {diff.months} tháng, {diff.days} ngày.")
except ValueError:
    print("Lỗi định dạng ngày.")
