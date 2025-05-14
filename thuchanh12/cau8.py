from datetime import datetime, timedelta

try:
    d = int(input("Nhập ngày: "))
    m = int(input("Nhập tháng: "))
    y = int(input("Nhập năm: "))
    current = datetime(y, m, d)
    prev_day = current - timedelta(days=1)
    print("Ngày trước đó:", prev_day.strftime("%d-%m-%Y"))
except Exception as e:
    print("Lỗi:", e)
