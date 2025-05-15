from datetime import datetime

try:
    d = int(input("Nhập ngày: "))
    m = int(input("Nhập tháng: "))
    y = int(input("Nhập năm: "))
    date = datetime(y, m, d)
    print("Ngày thuộc tuần thứ:", date.isocalendar().week)
except Exception as e:
    print("Lỗi:", e)
