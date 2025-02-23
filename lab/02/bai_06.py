so_nguyen = int(input("Nhập số nguyên có ba chữ số: "))

if 100 <= so_nguyen <= 999:
    hang_tram = so_nguyen // 100
    hang_chuc = (so_nguyen % 100) // 10
    hang_don_vi = so_nguyen % 10

    doc_hang_tram = ["không", "một", "hai", "ba", "bốn", "năm", "sáu", "bảy", "tám", "chín"]
    doc_hang_chuc = ["không", "mười", "hai mươi", "ba mươi", "bốn mươi", "năm mươi", "sáu mươi", "bảy mươi", "tám mươi", "chín mươi"]
    doc_hang_don_vi = ["không", "một", "hai", "ba", "bốn", "năm", "sáu", "bảy", "tám", "chín"]

    ket_qua = doc_hang_tram[hang_tram] + " trăm "
    if hang_chuc != 0:
        ket_qua += doc_hang_chuc[hang_chuc]
        if hang_don_vi != 0:
            ket_qua += " " + doc_hang_don_vi[hang_don_vi]
    elif hang_don_vi != 0:
        ket_qua += "lẻ " + doc_hang_don_vi[hang_don_vi]

    print(ket_qua)
else:
    print("Số không hợp lệ. Vui lòng nhập số có ba chữ số.")