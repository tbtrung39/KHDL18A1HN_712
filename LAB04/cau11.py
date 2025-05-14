import os
print('\n    CHƯƠNG TRÌNH GỌI ĐỒ UỐNG.')
while True :
    print('                                        ')
    print("|           Menu chọn chức năng         |")
    print("|[1] CAFE                               |")
    print("|[2] Cam vắt                            |")
    print("|[3] Nước ép cà rốt                     |")
    print("|[4] Nước lọc                           |")
    print("|[5] Nước dừa                           |")
    print("|[0] Bấm số 0 để thoát                  |")
    chon = int(input('Chọn chức năng cần thực hiện: '))
    if chon==1:
        print('CAFE')
    elif chon == 2:
        print('Cam vắt')
    elif chon == 3:
        print('Nước ép cà rốt')
    elif chon == 4:
        print('Nước lọc')    
    elif chon == 5:
        print('Nước dừa')
    elif chon == 0:
        break
    else:
        print('Chỉ chọn trong các số từ 1-5')
    tt = input("Nhấn phím bất kỳ để tiếp tục, bấm số 0 để thoát.")
    if tt == '0':
        break
    else: os.system('clc')