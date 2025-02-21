so_dien = float(input("NHập số Kw điện tiêu thụ : "))
tien_dien = 0 
if so_dien <= 100 : 
    tien_dien = 2000 * so_dien
elif so_dien <= 200 : 
    tien_dien = 2500 * so_dien 
elif so_dien <= 300 : 
    tien_dien == 3000 * so_dien 
else : 
    tien_dien  = 5000 * so_dien 
print(f"Tiền điện là {int(tien_dien)}  đồng")
