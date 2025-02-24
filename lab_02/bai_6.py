print("Chương trình đọc số nguyên có ba chữ số")
so = int(input("Nhập số nguyên có ba chữ số: "))
if 100 <= so <= 999:
    tram = so // 100
    chuc = (so // 10) % 10
    donvi = so % 10
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
    elif tram == 9:
        doc_tram = "Chín trăm"
    if chuc == 0:
        if donvi == 0:
            doc_chuc = ""
            doc_dv = ""
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
    elif chuc == 9:
        doc_chuc = "chín mươi"
    if donvi == 0:
        doc_dv = ""
    elif donvi == 1:
        if chuc > 1:
            doc_dv = "mốt"
        else:
            doc_dv = "một"
    elif donvi == 2:
        doc_dv = "hai"
    elif donvi == 3:
        doc_dv = "ba"
    elif donvi == 4:
        doc_dv = "bốn"
    elif donvi == 5:
        if chuc == 0:
            doc_dv = "năm"
        else:
            doc_dv = "lăm"
    elif donvi == 6:
        doc_dv = "sáu"
    elif donvi == 7:
        doc_dv = "bảy"
    elif donvi == 8:
        doc_dv = "tám"
    elif donvi == 9:
        doc_dv = "chín"
    if chuc == 0:
        print(doc_tram, doc_chuc, doc_dv)
    else:
        print(doc_tram, doc_chuc, doc_dv)
else:
    print("Vui lòng nhập lại")
