from datetime import datetime,timedelta
try:
    d = input("nhap ngay (dd-mm-yyyy)")
    date = datetime.strptime(d,"%d-%m-%Y")
    next_day = date + timedelta(days = 1)
    print("ngay ke tiep la: ", next_day.strftime("%d-%m-%Y"))
except:
    print("loi,dinh dang k hop le")
    