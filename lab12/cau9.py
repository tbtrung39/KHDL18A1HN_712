from datetime import datetime
try:
    d = input("Nhập ngày (dd-mm-yyyy): ")
    date = datetime.strptime(d, "%d-%m-%Y")
    thu = ["Thứ Hai", "Thứ Ba", "Thứ Tư", "Thứ Năm", "Thứ Sáu", "Thứ Bảy", "Chủ Nhật"]
    print("Ngày đó là:", thu[date.weekday()])
except:
    print("Loi.")