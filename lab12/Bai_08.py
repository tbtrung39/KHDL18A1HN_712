from datetime import datetime, timedelta
try:
    d = int(input("ngay: "))
    m = int(input("Thang: "))
    y = int(input("Nam: "))
    today = datetime(y,m,d)
    tomorrow = today - timedelta(days=1)
    print("Ngay tiep theo",tomorrow.strftime("%d-%m-%Y"))
except ValueError:
    print("Ngay khong hop le")
