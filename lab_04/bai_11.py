while True:
    print('---------MENU ĐỒ UỐNG----------')
    print('1. Cafe')
    print('2. Cam vắt')
    print('3. Nước ép cà rốt')
    print('4. Nước lọc')
    print('5. Nước dừa')
    print('0. Thoat chuong trinh')
    lua_chon = int(input('Vui lòng chọn đồ uống (1-5): '))
    print('Bạn đã chọn: ', end='')
    if lua_chon == 1: print('Cafe')
    elif lua_chon == 2: print('Cam vắt')
    elif lua_chon == 3: print('Nước ép cà rốt')
    elif lua_chon == 4: print('Nước lọc')
    elif lua_chon == 5: print('Nước dừa')
    elif lua_chon == 0: break
    else:
        print('Lựa chọn không hợp lệ! Vui lòng chọn số từ 1 đến 5.')