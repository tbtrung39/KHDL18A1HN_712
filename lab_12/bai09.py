from datetime import datetime

try:
    ngày = int(input("Nhập ngày: "))
    tháng = int(input("Nhập tháng: "))
    năm = int(input("Nhập năm: "))

    ngày_nhập = datetime(năm, tháng, ngày)
    thứ = ngày_nhập.strftime("%A")
    print("Ngày đó là thứ:", thứ)
except Exception as lỗi:
    print("Lỗi:", lỗi)