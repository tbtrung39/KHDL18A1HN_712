from datetime import datetime, timedelta
try:
    d = int(input("ngay: "))
    m = int(input("Thang: "))
    y = int(input("Nam: "))
    ngay_nhap = datetime(y,m,d)
    so_tuan = ngay_nhap.isocalendar().week
    print(f"ngay {ngay_nhap.strftime('%d-%m-%Y')} thuoc tuan thu {so_tuan} trong nam")
except ValueError:
    print("Loi")
    