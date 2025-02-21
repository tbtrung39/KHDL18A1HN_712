bat_dau = int(input("Nhập giờ bắt đầu(5h-->22h) : "))
ket_thuc = int(input("Nhập giờ kết thúc(5h-->22h): "))
gio = ket_thuc - bat_dau 
tien_thue = 0 
if bat_dau <= 5 or ket_thuc >=22  : 
    print("Nhập sai vui lòng nhập lại")
else : 
    if gio <= 3 : 
        tien_thue = gio * 100000 
        if bat_dau in (11,12,13,14) and ket_thuc in (12,13,14,15) : 
            tien_thue = tien_thue -(int(tien_thue *(10/100)))
    elif gio >=3 : 
        tien_thue = 300000 + (gio - 3) * 75000

        if bat_dau in (11,12,13,14) and ket_thuc in (12,13,14,15) : 
            tien_thue = tien_thue -(int(tien_thue *(10/100)))
print("Tiền thuê sân tập là : ", tien_thue )


