from datetime import datetime

def tinh_khoang_cach_ngay_thuan(ngay1_str, ngay2_str):
    try:
        ngay1 = datetime.strptime(ngay1_str, "%d-%m-%Y")
        ngay2 = datetime.strptime(ngay2_str, "%d-%m-%Y")
        if ngay1 > ngay2:
            ngay1, ngay2 = ngay2, ngay1
        tong_so_ngay = (ngay2 - ngay1).days
        nam = tong_so_ngay // 365
        ngay_con_lai = tong_so_ngay % 365
        thang = ngay_con_lai // 30
        ngay = ngay_con_lai % 30
        print(f"Hai ngay cach nhau: {nam} nam, {thang} thang, {ngay} ngay.")
    
    except ValueError:
        print("Loi dinh dang dd-mm-yyyy. Vui long nhap lai.")
ngay_thu_nhat = input("Nhap ngay thu nhat (dd-mm-yyyy): ")
ngay_thu_hai = input("Nhap ngay thu hai (dd-mm-yyyy): ")

tinh_khoang_cach_ngay_thuan(ngay_thu_nhat, ngay_thu_hai)