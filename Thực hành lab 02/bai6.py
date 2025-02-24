num = int(input("Nhập số nguyên có ba chữ số: "))
if num < 100 or num > 999:
    print("Số không hợp lệ, vui lòng nhập số có ba chữ số!")
else:
    tram = num // 100
    chuc = (num // 10) % 10
    don_vi = num % 10
    if tram == 1:
        doc_tram = "Một trăm"
    elif tram == 2:
        doc_tram = "Hai trăm"
    elif tram == 3:
        doc_tram = "Ba trăm"
    elif tram == 4:
        doc_tram = "Bốn trăm"
    elif tram == 5:
        doc_tram = "Năm trăm"
    elif tram == 6:
        doc_tram = "Sáu trăm"
    elif tram == 7:
        doc_tram = "Bảy trăm"
    elif tram == 8:
        doc_tram = "Tám trăm"
    else:
        doc_tram = "Chín trăm"
    # Đọc hàng chục
    if chuc == 0:
        if don_vi == 0:
            doc_chuc = ""
        else:
            doc_chuc = "lẻ"
    elif chuc == 1:
        doc_chuc = "mười"
    elif chuc == 2:
        doc_chuc = "hai mươi"
    elif chuc == 3:
        doc_chuc = "ba mươi"
    elif chuc == 4:
        doc_chuc = "bốn mươi"
    elif chuc == 5:
        doc_chuc = "năm mươi"
    elif chuc == 6:
        doc_chuc = "sáu mươi"
    elif chuc == 7:
        doc_chuc = "bảy mươi"
    elif chuc == 8:
        doc_chuc = "tám mươi"
    else:
        doc_chuc = "chín mươi"
    # Đọc hàng đơn vị
    if don_vi == 0:
        doc_dv = ""
    elif don_vi == 1:
        if chuc == 1 or chuc == 0:
            doc_dv = "một"
        else:
            doc_dv = "mốt"
    elif don_vi == 2:
        doc_dv = "hai"
    elif don_vi == 3:
        doc_dv = "ba"
    elif don_vi == 4:
        doc_dv = "bốn"
    elif don_vi == 5:
        if chuc == 0:
            doc_dv = "năm"
        else:
            doc_dv = "lăm"
    elif don_vi == 6:
        doc_dv = "sáu"
    elif don_vi == 7:
        doc_dv = "bảy"
    elif don_vi == 8:
        doc_dv = "tám"
    else:
        doc_dv = "chín"
    # In kết quả
    if doc_chuc == "" and doc_dv == "":
        print(doc_tram)
    else:
        print(doc_tram, doc_chuc, doc_dv)
