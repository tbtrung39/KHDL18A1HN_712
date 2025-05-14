from datetime import datetime

try:
    d = int(input("Ngày: "))
    m = int(input("Tháng: "))
    y = int(input("Năm: "))
    ngay = datetime(y, m, d)
    print("Ngày đó là:", ngay.strftime("%A"))
except Exception as e:
    print("Lỗi:", e)