tg = int(input("Nhập số giây tiêu thụ "))
W = 220 * 2.7 
kw = W / 1000 
kwh = kw * (tg / 3600 )
tiendien = 7000 * kwh 
print("tiền điện là ",kw , "đồng")