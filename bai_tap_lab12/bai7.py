from datetime import datetime, timedelta

try:
    d = input("Nhập ngày (dd-mm-yyyy): ")
    date = datetime.strptime(d, "%d-%m-%Y")
    next_day = date + timedelta(days=1)
    print("Ngày kế tiếp là:", next_day.strftime("%d-%m-%Y"))
except:
    print("Loi.")
