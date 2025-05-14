from datetime import datetime, timedelta

try:
    ngày = int(input("Nhập ngày: "))
    tháng = int(input("Nhập tháng: "))
    năm = int(input("Nhập năm: "))

    ngày_nhập = datetime(năm, tháng, ngày)
    ngày_trước = ngày_nhập - timedelta(days=1)

    print("Ngày trước đó là:", ngày_trước.strftime("%d-%m-%Y"))
except Exception as lỗi:
    print("Lỗi:", lỗi)