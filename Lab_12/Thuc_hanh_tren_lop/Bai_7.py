from datetime import datetime, timedelta

try:
    ngay = input("Nhap ngay (dd-mm-yyyy): ")
    d = datetime.strptime(ngay, "%d-%m-%Y") 
    ngay_mai = d + timedelta(days=1)

    print("Ngay ke tiep:", ngay_mai.strftime("%d-%m-%Y"))

except ValueError:
    print("Loi dinh dang (dd-mm-yyyy)")
