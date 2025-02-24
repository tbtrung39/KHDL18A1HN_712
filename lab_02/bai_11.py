print("Chương trình tính ngày tiếp theo")
ng = int(input("Nhập ngày: "))
th = int(input("Nhập tháng: "))

if 1 <= th <= 12 and 1 <= ng <= 31:
    if th == 2:
        if ng > 28:
            print("Ngày không hợp lệ")
        elif ng == 28:
            ng = 1
            th = 3
            print("Ngày tiếp theo là", ng, "/", th)
        else:
            ng += 1
            print("Ngày tiếp theo là", ng, "/", th)

    elif th == 4:
        if ng > 30:
            print("Ngày không hợp lệ")
        elif ng == 30:
            ng = 1
            th = 5
            print("Ngày tiếp theo là", ng, "/", th)
        else:
            ng += 1
            print("Ngày tiếp theo là", ng, "/", th)

    elif th == 6:
        if ng > 30:
            print("Ngày không hợp lệ")
        elif ng == 30:
            ng = 1
            th = 7
            print("Ngày tiếp theo là", ng, "/", th)
        else:
            ng += 1
            print("Ngày tiếp theo là", ng, "/", th)

    elif th == 9:
        if ng > 30:
            print("Ngày không hợp lệ")
        elif ng == 30:
            ng = 1
            th = 10
            print("Ngày tiếp theo là", ng, "/", th)
        else:
            ng += 1
            print("Ngày tiếp theo là", ng, "/", th)

    elif th == 11:
        if ng > 30:
            print("Ngày không hợp lệ")
        elif ng == 30:
            ng = 1
            th = 12
            print("Ngày tiếp theo là", ng, "/", th)
        else:
            ng += 1
            print("Ngày tiếp theo là", ng, "/", th)

    elif th == 1:
        if ng > 31:
            print("Ngày không hợp lệ")
        elif ng == 31:
            ng = 1
            th = 2
            print("Ngày tiếp theo là", ng, "/", th)
        else:
            ng += 1
            print("Ngày tiếp theo là", ng, "/", th)

    elif th == 3:
        if ng > 31:
            print("Ngày không hợp lệ")
        elif ng == 31:
            ng = 1
            th = 4
            print("Ngày tiếp theo là", ng, "/", th)
        else:
            ng += 1
            print("Ngày tiếp theo là", ng, "/", th)

    elif th == 5:
        if ng > 31:
            print("Ngày không hợp lệ")
        elif ng == 31:
            ng = 1
            th = 6
            print("Ngày tiếp theo là", ng, "/", th)
        else:
            ng += 1
            print("Ngày tiếp theo là", ng, "/", th)

    elif th == 7:
        if ng > 31:
            print("Ngày không hợp lệ")
        elif ng == 31:
            ng = 1
            th = 8
            print("Ngày tiếp theo là", ng, "/", th)
        else:
            ng += 1
            print("Ngày tiếp theo là", ng, "/", th)

    elif th == 8:
        if ng > 31:
            print("Ngày không hợp lệ")
        elif ng == 31:
            ng = 1
            th = 9
            print("Ngày tiếp theo là", ng, "/", th)
        else:
            ng += 1
            print("Ngày tiếp theo là", ng, "/", th)

    elif th == 10:
        if ng > 31:
            print("Ngày không hợp lệ")
        elif ng == 31:
            ng = 1
            th = 11
            print("Ngày tiếp theo là", ng, "/", th)
        else:
            ng += 1
            print("Ngày tiếp theo là", ng, "/", th)

    elif th == 12:
        if ng > 31:
            print("Ngày không hợp lệ")
        elif ng == 31:
            ng = 1
            th = 1
            print("Ngày tiếp theo là", ng, "/", th)
        else:
            ng += 1
            print("Ngày tiếp theo là", ng, "/", th)

else:
    print("Ngày hoặc tháng không hợp lệ")
