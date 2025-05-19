from datetime import datetime,timedelta
try:
    d = input("nhap ngay (dd-mm-yyyy)")
    date = datetime.strptime(d,"%d-%m%Y")
    prev_day = date - timedelta(days = 1)
    print("ngay trc do la: ",prev_day.strftime("%d-%m-%Y"))
except:
    prev_day("loi,dinh dang ko hop le")
