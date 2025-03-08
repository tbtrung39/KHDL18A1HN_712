#Câu 11:
print('\nMENU ĐỒ UỐNG')
while True:
    print("____________________________")
    print("|Menu chọn đồ uống         |")
    print("|1.cafe                    |")
    print("|2.cam vắt                 |")
    print("|3.nước ép cà rốt          |")
    print("|4.nước lọc                |")
    print("|5.nước dừa                |")
    print("|0.thoát                   |")
 
    chon=int(input("chọn thức uống từ 1-5"))
    if chon==1:
        print("Bạn đã chọn cafe")
    elif chon==2:
        print("Bạn đã chọn cam vắt")
    elif chon==3:
        print("Bạn đã chọn nước ép cà rốt")
    elif chon==4:
        print("Bạn đã chọn nước lọc")
    elif chon==5:
        print("Bạn đã chọn nước dừa")
    elif chon==0:
        break
    else:
        print("Lựa chọn không hợp lệ hãy nhập lại")
        break