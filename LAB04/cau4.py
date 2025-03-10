while True:
    tu_so = int(input("Nhập tử số: "))
    mau_so = int(input("Nhập mẫu số: "))

    if mau_so != 0:
        print("Phân số hợp lệ:", tu_so, "/", mau_so)
        break
    else:
        print("Mẫu số không thể bằng 0. Vui lòng nhập lại.")