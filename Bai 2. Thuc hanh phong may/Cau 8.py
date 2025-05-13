# Cau 8.

import datetime
def nhap_ngay():
    try:
        ngay = int(input("Nhap ngay: "))
        thang = int(input("Nhap thang: "))
        nam = int(input("Nhap nam: "))
        return datetime.date(nam, thang, ngay)
    except ValueError:
        print("Ngay thang nam khong hop le.")
        return None
def tim_ngay_truoc_do(ngay_hien_tai):
    return ngay_hien_tai - datetime.timedelta(days=1)
def chay_bai_8():
    ngay = nhap_ngay()
    if ngay is None:
        print("Khong the xu ly vi ngay nhap sai.")
        return
    ngay_truoc = tim_ngay_truoc_do(ngay)
    print(f"Ngay truoc do la: {ngay_truoc.strftime('%d-%m-%Y')}")
chay_bai_8()
