from datetime import datetime, timedelta

day = int(input("Nhập ngày: "))
month = int(input("Nhập tháng: "))
year = 2025  # Năm không nhuận

try:
    date = datetime(year, month, day)
    next_day = date + timedelta(days=1)
    print(f"Ngày tiếp theo là: {next_day.day}/{next_day.month}")
except ValueError:
    print("Ngày không hợp lệ!")