from datetime import datetime, timedelta

try:
    date_str = input("Nhập ngày (dd-mm-yyyy): ")
    date_obj = datetime.strptime(date_str, "%d-%m-%Y")
    prev_day = date_obj - timedelta(days=1)
    print("Ngày trước đó là:", prev_day.strftime("%d-%m-%Y"))
except ValueError:
    print("Định dạng ngày không hợp lệ.")
