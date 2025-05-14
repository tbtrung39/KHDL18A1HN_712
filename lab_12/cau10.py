from datetime import datetime

try:
    ngay1 = input("Nhập ngày 1 (dd-mm-yyyy): ")
    ngay2 = input("Nhập ngày 2 (dd-mm-yyyy): ")

    d1 = datetime.strptime(ngay1, "%d-%m-%Y")
    d2 = datetime.strptime(ngay2, "%d-%m-%Y")

    if d1 > d2:
        d1, d2 = d2, d1

    khoang_cach = d2 - d1
    nam = khoang_cach.days // 365
    thang = (khoang_cach.days % 365) // 30
    ngay = (khoang_cach.days % 365) % 30

    print(f"Hai ngày cách nhau {nam} năm, {thang} tháng, {ngay} ngày.")
except Exception as e:
    print("Lỗi:", e)