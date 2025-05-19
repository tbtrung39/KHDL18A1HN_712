from datetime import datetime,timedelta
try:
    d = input("nhap ngay (dd-mm-yyyy)")
    date = datetime.strptime(d,"%d-%m%Y")
    thu = ["thu hai","thu ba","thu tu", "thu nam","thu sau","thu bay","chu nhat"]
    print("ngay do la:",thu[date.weekday()])
except:
    print("loi")