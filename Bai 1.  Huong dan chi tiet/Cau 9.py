# Cau 9.

import datetime
def week_of_date(date_string):
    try:
        date_obj = datetime.datetime.strptime(date_string, '%d-%m-%Y').date()
        start_of_week = date_obj - datetime.timedelta(days=date_obj.weekday())
        
        for i in range(7):
            day = start_of_week + datetime.timedelta(days=i)
            print(day.strftime('%A, %d-%m-%Y')) 
    except ValueError:
        print("Dinh dang ngay khong hop le. Vui long nhap lai theo dinh dang 'dd-mm-yyyy'.")
date_str = input("Nhap ngay theo dinh dang (dd-mm-yyyy): ")
week_of_date(date_str)
