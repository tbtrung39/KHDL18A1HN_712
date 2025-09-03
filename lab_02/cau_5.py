thu=int(input("nhap thang trong nam: "))
if thu >=1 and thu<=12:
    if thu==1:
        print(thu,":January")
    elif thu==2:
        print(thu,":February")
    elif thu==3:
        print(thu,":March")
    elif thu==4:
        print(thu,":April")
    elif thu==5:
        print(thu,":May")
    elif thu==6:
        print(thu,":June")
    elif thu==7:
        print(thu,":July")
    elif thu==8:
        print(thu,":August")
    elif thu==9:
        print(thu,":September")
    elif thu==10:
        print(thu,":October")
    elif thu==11:
        print(thu,":November")
    elif thu==12:
        print(thu,":December")
else:
    print("nhap sai. vui long nhap lai")