from datetime import datetime, timedelta
try:
    d = input("Nhập ngày (dd-mm-yyyy): ")
    date = datetime.strptime(d, "%d-%m-%Y")
    prev_day = date - timedelta(days=1)
    print("Ngày trước đó là:", prev_day.strftime("%d-%m-%Y"))
except:
    print("Loi.")