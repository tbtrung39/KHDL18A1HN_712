from datetime import datetime, timedelta

try:
    ngay = input("Nhap ngay (dd-mm-yyyy): ")
    d = datetime.strptime(ngay, "%d-%m-%Y") 
    hom_qua = d - timedelta(days=1) 
    print("Ngay truoc do:", hom_qua.strftime("%d-%m-%Y"))

except ValueError:
    print("Loi dinh dang (dd-mm-yyyy)")
