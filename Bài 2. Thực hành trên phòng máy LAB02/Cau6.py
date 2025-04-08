# Cau 6.
so_nguyen = int(input("Nhập vào một số nguyên có ba chữ số: "))
if 100 <= so_nguyen <= 999 or -999 <= so_nguyen <= -100:    
    so_nguyen = abs(so_nguyen)   
    tram = so_nguyen // 100
    chuc = (so_nguyen // 10) % 10
    don_vi = so_nguyen % 10   
    if tram == 1:
        ket_qua = "một trăm"
    elif tram == 2:
        ket_qua = "hai trăm"
    elif tram == 3:
        ket_qua = "ba trăm"
    elif tram == 4:
        ket_qua = "bốn trăm"
    elif tram == 5:
        ket_qua = "năm trăm"
    elif tram == 6:
        ket_qua = "sáu trăm"
    elif tram == 7:
        ket_qua = "bảy trăm"
    elif tram == 8:
        ket_qua = "tám trăm"
    elif tram == 9:
        ket_qua = "chín trăm"        
    if chuc == 0 and don_vi != 0:
        ket_qua += " linh"
        if don_vi == 1:
            ket_qua += " một"
        elif don_vi == 2:
            ket_qua += " hai"
        elif don_vi == 3:
            ket_qua += " ba"
        elif don_vi == 4:
            ket_qua += " bốn"
        elif don_vi == 5:
            ket_qua += " năm"
        elif don_vi == 6:
            ket_qua += " sáu"
        elif don_vi == 7:
            ket_qua += " bảy"
        elif don_vi == 8:
            ket_qua += " tám"
        elif don_vi == 9:
            ket_qua += " chín"
    elif chuc == 1:
        ket_qua += " mười"
        if don_vi == 1:
            ket_qua += " một"
        elif don_vi == 2:
            ket_qua += " hai"
        elif don_vi == 3:
            ket_qua += " ba"
        elif don_vi == 4:
            ket_qua += " bốn"
        elif don_vi == 5:
            ket_qua += " lăm"
        elif don_vi == 6:
            ket_qua += " sáu"
        elif don_vi == 7:
            ket_qua += " bảy"
        elif don_vi == 8:
            ket_qua += " tám"
        elif don_vi == 9:
            ket_qua += " chín"
    elif chuc > 1:
        if chuc == 2:
            ket_qua += " hai mươi"
        elif chuc == 3:
            ket_qua += " ba mươi"
        elif chuc == 4:
            ket_qua += " bốn mươi"
        elif chuc == 5:
            ket_qua += " năm mươi"
        elif chuc == 6:
            ket_qua += " sáu mươi"
        elif chuc == 7:
            ket_qua += " bảy mươi"
        elif chuc == 8:
            ket_qua += " tám mươi"
        elif chuc == 9:
            ket_qua += " chín mươi"        
        if don_vi == 1:
            ket_qua += " mốt"
        elif don_vi == 2:
            ket_qua += " hai"
        elif don_vi == 3:
            ket_qua += " ba"
        elif don_vi == 4:
            ket_qua += " bốn"
        elif don_vi == 5:
            ket_qua += " lăm"
        elif don_vi == 6:
            ket_qua += " sáu"
        elif don_vi == 7:
            ket_qua += " bảy"
        elif don_vi == 8:
            ket_qua += " tám"
        elif don_vi == 9:
            ket_qua += " chín"
    else:
        ket_qua += ""   
    print("Cách đọc:", ket_qua)
else:
    print("Vui lòng nhập một số nguyên có ba chữ số.")
