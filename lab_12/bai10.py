from datetime import datetime

ngay1_chuoi = input("Nhập ngày thứ nhất (dd-mm-yyyy): ")
ngay2_chuoi = input("Nhập ngày thứ hai (dd-mm-yyyy): ")
dinh_dang = "%d-%m-%Y"

ngay1 = datetime.strptime(ngay1_chuoi, dinh_dang)
ngay2 = datetime.strptime(ngay2_chuoi, dinh_dang)

so_ngay_chenh_lech = abs((ngay2 - ngay1).days)
so_nam = so_ngay_chenh_lech // 365
so_ngay_con_lai = so_ngay_chenh_lech % 365

so_thang = so_ngay_con_lai // 30
so_ngay = so_ngay_con_lai % 30
print(f"Hai ngày cách nhau khoảng {so_nam} năm, {so_thang} tháng, {so_ngay} ngày.")

