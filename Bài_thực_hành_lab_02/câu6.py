cac_chu_so = ["", "Một", "Hai", "Ba", "Bốn", "Năm", "Sáu", "Bảy", "Tám", "Chín"]

so = int(input("Nhập số nguyên có ba chữ số: "))

if 100 <= so <= 999:
    hang_tram = so // 100
    hang_chuc = (so // 10) % 10
    hang_don_vi = so % 10

    ket_qua = f"{cac_chu_so[hang_tram]} trăm"
    
    if hang_chuc == 0 and hang_don_vi != 0:
        ket_qua += f" lẻ {cac_chu_so[hang_don_vi]}"
    elif hang_chuc == 1:
        if hang_don_vi == 0:
            ket_qua += " mười"
        elif hang_don_vi == 5:
            ket_qua += " mười lăm"
        else:
            ket_qua += f" mười {cac_chu_so[hang_don_vi]}"
    else:
        if hang_chuc != 0:
            ket_qua += f" {cac_chu_so[hang_chuc]} mươi"
        if hang_don_vi == 5:
            ket_qua += " lăm"
        elif hang_don_vi != 0:
            ket_qua += f" {cac_chu_so[hang_don_vi]}"
    
    print(f"Cách đọc: {ket_qua}")
else:
    print("Vui lòng nhập số nguyên có đúng 3 chữ số!")
