from datetime import datetime

try:
    d = int(input("Ngày: "))
    m = int(input("Tháng: "))
    y = int(input("Năm: "))
    ngay = datetime(y, m, d)
    if ngay >= datetime.now():
        raise ValueError("Ngày phải trước ngày hiện tại")
    print("Ngày hợp lệ:", ngay.strftime("%d-%m-%Y"))
except Exception as e:
    print("Lỗi:", e)