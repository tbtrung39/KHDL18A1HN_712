# Cau 10.

from datetime import datetime
from dateutil.relativedelta import relativedelta
def nhap_ngay(text):
    try:
        chuoi = input(f"Nhap {text} (dd-mm-yyyy): ")
        ngay = datetime.strptime(chuoi, "%d-%m-%Y")
        return ngay
    except ValueError:
        print("Dinh dang ngay khong hop le.")
        return None
def tinh_khoang_cach(ngay1, ngay2):
    if ngay1 > ngay2:
        ngay1, ngay2 = ngay2, ngay1
    hieu = relativedelta(ngay2, ngay1)
    return hieu.years, hieu.months, hieu.days
def chay_bai_10():
    ngay1 = nhap_ngay("ngay thu nhat")
    ngay2 = nhap_ngay("ngay thu hai")
    if ngay1 is None or ngay2 is None:
        print("Khong the tinh do lech vi ngay nhap sai.")
        return
    nam, thang, ngay = tinh_khoang_cach(ngay1, ngay2)
    print(f"Hai ngay cach nhau: {nam} nam, {thang} thang, {ngay} ngay.")
chay_bai_10()