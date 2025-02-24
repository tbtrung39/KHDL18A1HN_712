def doc_ba_chu_so(so):
    hang_tram = so // 100
    hang_chuc = (so % 100) // 10
    hang_don_vi = so % 10
    chu_so = ["không", "một", "hai", "ba", "bốn", "năm", "sáu", "bảy", "tám", "chín"]
    if hang_tram == 0:
        return "Số nhập vào không phải là số có ba chữ số"
    doc_tram = chu_so[hang_tram] + " trăm"
    doc_chuc = chu_so[hang_chuc] + " mươi" if hang_chuc != 0 else "lẻ"
    doc_don_vi = chu_so[hang_don_vi]
    if hang_chuc == 0 and hang_don_vi != 0:
        doc_chuc = "lẻ"
    if hang_chuc == 1:
        doc_chuc = "mười"
    if hang_chuc > 1 and hang_don_vi == 0:
        doc_don_vi = ""
    if hang_don_vi == 1:
        doc_don_vi = "mốt"
    if hang_chuc > 1 and hang_don_vi == 5:
        doc_don_vi = "lăm"
    return doc_tram + " " + doc_chuc + " " + doc_don_vi

so = int(input("Nhập vào một số nguyên có ba chữ số: "))
print(doc_ba_chu_so(so))
