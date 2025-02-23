sodien = float(input("Nhap so KW dien tieu thu: "))
if sodien >=0:
    if sodien >300:
        print("so tien dien can tra la: ",sodien*5000)
    elif sodien >200:
        print("so tien dien can tra la: ",sodien*3000)
    elif sodien >100:
        print("so tien dien can tra la: ",sodien*2500)
    else:
        print("so tien dien can tra la: ",sodien*2000)
else:
    print("so dien nhap vao loi. Vui long nhap lai")