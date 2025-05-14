from datetime import datetime

try:
    d = int(input("Ngày: "))
    m = int(input("Tháng: "))
    y = int(input("Năm: "))
    ngay = datetime(y, m, d)
    print("Ngày thứ", ngay.timetuple().tm_yday, "trong năm")
except Exception as e:
    print("Lỗi:", e)