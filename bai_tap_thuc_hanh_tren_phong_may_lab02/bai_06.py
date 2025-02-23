n = int(input("Nhập vào một số nguyên có ba chữ số: "))

if 100 <= n <= 999 or -999 <= n <= -100:
    if n < 0:
        print("Âm", end=" ")
        n = -n
    
    tram = n // 100
    chuc = (n // 10) % 10
    don_vi = n % 10
    
    if tram == 1:
        print("Một trăm", end=" ")
    elif tram == 2:
        print("Hai trăm", end=" ")
    elif tram == 3:
        print("Ba trăm", end=" ")
    elif tram == 4:
        print("Bốn trăm", end=" ")
    elif tram == 5:
        print("Năm trăm", end=" ")
    elif tram == 6:
        print("Sáu trăm", end=" ")
    elif tram == 7:
        print("Bảy trăm", end=" ")
    elif tram == 8:
        print("Tám trăm", end=" ")
    elif tram == 9:
        print("Chín trăm", end=" ")
    
    if chuc == 0 and don_vi != 0:
        print("lẻ", end=" ")
    elif chuc == 1:
        print("Mười", end=" ")
    elif chuc == 2:
        print("Hai mươi", end=" ")
    elif chuc == 3:
        print("Ba mươi", end=" ")
    elif chuc == 4:
        print("Bốn mươi", end=" ")
    elif chuc == 5:
        print("Năm mươi", end=" ")
    elif chuc == 6:
        print("Sáu mươi", end=" ")
    elif chuc == 7:
        print("Bảy mươi", end=" ")
    elif chuc == 8:
        print("Tám mươi", end=" ")
    elif chuc == 9:
        print("Chín mươi", end=" ")
    
    if don_vi == 1 and chuc > 1:
        print("mốt")
    elif don_vi == 5 and chuc > 0:
        print("lăm")
    elif don_vi == 1:
        print("Một")
    elif don_vi == 2:
        print("Hai")
    elif don_vi == 3:
        print("Ba")
    elif don_vi == 4:
        print("Bốn")
    elif don_vi == 5:
        print("Năm")
    elif don_vi == 6:
        print("Sáu")
    elif don_vi == 7:
        print("Bảy")
    elif don_vi == 8:
        print("Tám")
    elif don_vi == 9:
        print("Chín")
else:
    print("Vui lòng nhập một số có ba chữ số.")
