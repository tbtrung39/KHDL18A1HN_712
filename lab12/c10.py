from datetime import datetime
try:
    d1 = datetime.strptime(input("Ngay 1 (dd-mm-yyyy): "),"%d-%m-%Y")
    d2 = datetime.strptime(input("Ngay 2 (dd-mm-yyyy): "),"%d-%m-%Y")
    delta = abs((d2 - d1).days)
    years,rem = divmod(delta,365)
    months,days = divmod(rem,30)
    print(f"cach nhau: {years} nam,{months} thang,{days} ngay.")
except:
    print('loi')