from datetime import datetime

try:
    date_str = input("Nhập ngày (dd-mm-yyyy): ")
    date_obj = datetime.strptime(date_str, "%d-%m-%Y")
    thu = date_obj.weekday()  # 0=Thứ 2, 6=Chủ nhật

    if thu == 5:
        print("Đó là Thứ Bảy.")
    elif thu == 6:
        print("Đó là Chủ Nhật.")
    else:
        print("Không phải Thứ Bảy hoặc Chủ Nhật.")
except ValueError:
    print("Định dạng ngày không hợp lệ.")
