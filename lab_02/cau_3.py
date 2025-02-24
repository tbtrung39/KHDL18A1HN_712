thu=int(input("nhap thu trong tuan: "))
if thu >=1 and thu<=7:
    if thu==1:
        print(thu,":sunday")
    elif thu==2:
        print(thu,":monday")
    elif thu==3:
        print(thu,":Tuesday")
    elif thu==4:
        print(thu,":Wednesday")
    elif thu==5:
        print(thu,":Thursday")
    elif thu==6:
        print(thu,":Friday")
    elif thu==7:
        print(thu,":Saturday")
else:
    print("nhap sai. vui long nhap lai")