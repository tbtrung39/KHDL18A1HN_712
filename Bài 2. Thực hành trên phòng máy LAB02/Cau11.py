# Cau 11.
ngay = int(input("Nhập ngày: "))
thang = int(input("Nhập tháng: "))
if thang < 1 or thang > 12:
    print("Tháng không hợp lệ!")
elif thang == 1:
    if ngay < 1 or ngay > 31:
        print("Ngày không hợp lệ!")
    elif ngay == 31:
        ngay_tiep_theo = 1
        thang_tiep_theo = 2
        print(f"Ngày tiếp theo là: {ngay_tiep_theo}/{thang_tiep_theo}")
    else:
        ngay_tiep_theo = ngay + 1
        thang_tiep_theo = thang
        print(f"Ngày tiếp theo là: {ngay_tiep_theo}/{thang_tiep_theo}")
elif thang == 2:
    if ngay < 1 or ngay > 28:
        print("Ngày không hợp lệ!")
    elif ngay == 28:
        ngay_tiep_theo = 1
        thang_tiep_theo = 3
        print(f"Ngày tiếp theo là: {ngay_tiep_theo}/{thang_tiep_theo}")
    else:
        ngay_tiep_theo = ngay + 1
        thang_tiep_theo = thang
        print(f"Ngày tiếp theo là: {ngay_tiep_theo}/{thang_tiep_theo}")
elif thang == 3:
    if ngay < 1 or ngay > 31:
        print("Ngày không hợp lệ!")
    elif ngay == 31:
        ngay_tiep_theo = 1
        thang_tiep_theo = 4
        print(f"Ngày tiếp theo là: {ngay_tiep_theo}/{thang_tiep_theo}")
    else:
        ngay_tiep_theo = ngay + 1
        thang_tiep_theo = thang
        print(f"Ngày tiếp theo là: {ngay_tiep_theo}/{thang_tiep_theo}")
elif thang == 4:
    if ngay < 1 or ngay > 30:
        print("Ngày không hợp lệ!")
    elif ngay == 30:
        ngay_tiep_theo = 1
        thang_tiep_theo = 5
        print(f"Ngày tiếp theo là: {ngay_tiep_theo}/{thang_tiep_theo}")
    else:
        ngay_tiep_theo = ngay + 1
        thang_tiep_theo = thang
        print(f"Ngày tiếp theo là: {ngay_tiep_theo}/{thang_tiep_theo}")
elif thang == 5:
    if ngay < 1 or ngay > 31:
        print("Ngày không hợp lệ!")
    elif ngay == 31:
        ngay_tiep_theo = 1
        thang_tiep_theo = 6
        print(f"Ngày tiếp theo là: {ngay_tiep_theo}/{thang_tiep_theo}")
    else:
        ngay_tiep_theo = ngay + 1
        thang_tiep_theo = thang
        print(f"Ngày tiếp theo là: {ngay_tiep_theo}/{thang_tiep_theo}")
elif thang == 6:
    if ngay < 1 or ngay > 30:
        print("Ngày không hợp lệ!")
    elif ngay == 30:
        ngay_tiep_theo = 1
        thang_tiep_theo = 7
        print(f"Ngày tiếp theo là: {ngay_tiep_theo}/{thang_tiep_theo}")
    else:
        ngay_tiep_theo = ngay + 1
        thang_tiep_theo = thang
        print(f"Ngày tiếp theo là: {ngay_tiep_theo}/{thang_tiep_theo}")
elif thang == 7:
    if ngay < 1 or ngay > 31:
        print("Ngày không hợp lệ!")
    elif ngay == 31:
        ngay_tiep_theo = 1
        thang_tiep_theo = 8
        print(f"Ngày tiếp theo là: {ngay_tiep_theo}/{thang_tiep_theo}")
    else:
        ngay_tiep_theo = ngay + 1
        thang_tiep_theo = thang
        print(f"Ngày tiếp theo là: {ngay_tiep_theo}/{thang_tiep_theo}")
elif thang == 8:
    if ngay < 1 or ngay > 31:
        print("Ngày không hợp lệ!")
    elif ngay == 31:
        ngay_tiep_theo = 1
        thang_tiep_theo = 9
        print(f"Ngày tiếp theo là: {ngay_tiep_theo}/{thang_tiep_theo}")
    else:
        ngay_tiep_theo = ngay + 1
        thang_tiep_theo = thang
        print(f"Ngày tiếp theo là: {ngay_tiep_theo}/{thang_tiep_theo}")
elif thang == 9:
    if ngay < 1 or ngay > 30:
        print("Ngày không hợp lệ!")
    elif ngay == 30:
        ngay_tiep_theo = 1
        thang_tiep_theo = 10
        print(f"Ngày tiếp theo là: {ngay_tiep_theo}/{thang_tiep_theo}")
    else:
        ngay_tiep_theo = ngay + 1
        thang_tiep_theo = thang
        print(f"Ngày tiếp theo là: {ngay_tiep_theo}/{thang_tiep_theo}")
elif thang == 10:
    if ngay < 1 or ngay > 31:
        print("Ngày không hợp lệ!")
    elif ngay == 31:
        ngay_tiep_theo = 1
        thang_tiep_theo = 11
        print(f"Ngày tiếp theo là: {ngay_tiep_theo}/{thang_tiep_theo}")
    else:
        ngay_tiep_theo = ngay + 1
        thang_tiep_theo = thang
        print(f"Ngày tiếp theo là: {ngay_tiep_theo}/{thang_tiep_theo}")
elif thang == 11:
    if ngay < 1 or ngay > 30:
        print("Ngày không hợp lệ!")
    elif ngay == 30:
        ngay_tiep_theo = 1
        thang_tiep_theo = 12
        print(f"Ngày tiếp theo là: {ngay_tiep_theo}/{thang_tiep_theo}")
    else:
        ngay_tiep_theo = ngay + 1
        thang_tiep_theo = thang
        print(f"Ngày tiếp theo là: {ngay_tiep_theo}/{thang_tiep_theo}")
elif thang == 12:
    if ngay < 1 or ngay > 31:
        print("Ngày không hợp lệ!")
    elif ngay == 31:
        ngay_tiep_theo = 1
        thang_tiep_theo = 1
        print(f"Ngày tiếp theo là: {ngay_tiep_theo}/{thang_tiep_theo}")
    else:
        ngay_tiep_theo = ngay + 1
        thang_tiep_theo = thang
        print(f"Ngày tiếp theo là: {ngay_tiep_theo}/{thang_tiep_theo}")
else:
    print("Tháng không hợp lệ!")