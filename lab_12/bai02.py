chuỗi = input("Nhập chuỗi ký tự: ")

if not chuỗi.isalpha():
    print("Lỗi ký tự !!!")
else:
    lỗi = False
    for i in range(len(chuỗi) - 1):
        if chuỗi[i] == chuỗi[i + 1]:
            print("Lỗi nhập liệu !!!")
            lỗi = True
            break

    if not lỗi:
        for i in range(len(chuỗi) - 3):
            if chuỗi[i] == chuỗi[i+1] == chuỗi[i+2] == chuỗi[i+3]:
                print("Lỗi nhập lặp lại !!!")
                lỗi = True
                break

    if not lỗi:
        for i in range(len(chuỗi) - 4):
            if chuỗi[i] == chuỗi[i+1] == chuỗi[i+2] == chuỗi[i+3] == chuỗi[i+4]:
                print("Lỗi nhập trùng lặp !!!")
                lỗi = True
                break

    if not lỗi:
        print("Chuỗi hợp lệ.")
