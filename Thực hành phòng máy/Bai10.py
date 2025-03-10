so = int(input("Nhập một số nguyên dương: "))
while so < 0:
    print("Vui lòng nhập số nguyên dương!")
    so = int(input("Nhập một số nguyên dương: "))
if so == 0:
    print("không")
else:
    so_dao = 0
    tam = so
    while tam > 0:
        so_dao = so_dao * 10 + tam % 10
        tam //= 10
    while so_dao > 0:
        chu_so = so_dao % 10
        if chu_so == 0:
            print("không", end=" ")
        elif chu_so == 1:
            print("một", end=" ")
        elif chu_so == 2:
            print("hai", end=" ")
        elif chu_so == 3:
            print("ba", end=" ")
        elif chu_so == 4:
            print("bốn", end=" ")
        elif chu_so == 5:
            print("năm", end=" ")
        elif chu_so == 6:
            print("sáu", end=" ")
        elif chu_so == 7:
            print("bảy", end=" ")
        elif chu_so == 8:
            print("tám", end=" ")
        elif chu_so == 9:
            print("chín", end=" ")

        so_dao //= 10
