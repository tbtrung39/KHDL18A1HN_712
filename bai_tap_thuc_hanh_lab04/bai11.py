while True:
    print("\nMenu đồ uống:")
    print("1. Cafe")
    print("2. Cam vắt")
    print("3. Nước ép cà rốt")
    print("4. Nước lọc")
    print("5. Nước dừa")
    print("0. Thoat chuong trinh")
    lua_chon = int(input("Vui lòng chọn đồ uống (1-5): "))
    if lua_chon == 1:
        print("Bạn đã chọn: Cafe")
        break
    elif lua_chon == 2:
        print("Bạn đã chọn: Cam vắt")
        break
    elif lua_chon == 3:
        print("Bạn đã chọn: Nước ép cà rốt")
        break
    elif lua_chon == 4:
        print("Bạn đã chọn: Nước lọc")
        break
    elif lua_chon == 5:
        print("Bạn đã chọn: Nước dừa")
        break
    elif lua_chon == 0:
        print(" thoát ")
    else:
        print("Lựa chọn không hợp lệ! Vui lòng chọn số từ 1 đến 5.")