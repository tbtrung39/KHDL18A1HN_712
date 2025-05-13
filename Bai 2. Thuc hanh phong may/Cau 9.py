# Cau 9.

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
def tinh_tuan(ngay):
    return ngay.isocalendar()[1]
def chay_bai_9():
    ngay = nhap_ngay()
    if ngay is None:
        print("Khong the tinh vi ngay nhap sai!!")
        return
    tuan = tinh_tuan(ngay)
    print(f"Ngay {ngay.strftime('%d-%m-%Y')} thuoc tuan thu {tuan} trong nam. ")
chay_bai_9()
