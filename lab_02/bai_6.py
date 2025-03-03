def doc_so_nguyen_ba_chu_so(so):
    if not (100 <= so <= 999):
        return "Số không hợp lệ"
    hang_tram = so // 100
    hang_chuc = (so % 100) // 10
    hang_dv = so % 10
    doc_hang_tram = {1: "một trăm", 2: "hai trăm", 3: "ba trăm", 4: "bốn trăm", 5: "năm trăm", 6: "sáu trăm", 7: "bảy trăm", 8: "tám trăm", 9: "chín trăm"}
    doc_hang_chuc = {0: "", 1: "mười", 2: "hai mươi", 3: "ba mươi", 4: "bốn mươi", 5: "năm mươi", 6: "sáu mươi", 7: "bảy mươi", 8: "tám mươi", 9: "chín mươi"}
    doc_hang_dv = {0: "", 1: "một", 2: "hai", 3: "ba", 4: "bốn", 5: "năm", 6: "sáu", 7: "bảy", 8: "tám", 9: "chín"}

    ket_qua = doc_hang_tram[hang_tram]
    if hang_chuc != 0:
        ket_qua += " " + doc_hang_chuc[hang_chuc]
    if hang_dv != 0:
        ket_qua += " " + doc_hang_dv[hang_dv]
    return ket_qua