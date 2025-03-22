so = int(input("Nhập số nguyên có ba chữ số: "))
hang_tram = so // 100
hang_chuc = (so // 10) % 10
hang_don_vi = so % 10

doc_hang_tram = ["", "Một trăm", "Hai trăm", "Ba trăm", "Bốn trăm", "Năm trăm", "Sáu trăm", "Bảy trăm", "Tám trăm", "Chín trăm"]
doc_hang_chuc = ["", "mười", "hai mươi", "ba mươi", "bốn mươi", "năm mươi", "sáu mươi", "bảy mươi", "tám mươi", "chín mươi"]
doc_hang_don_vi = ["", "một", "hai", "ba", "bốn", "năm", "sáu", "bảy", "tám", "chín"]

print(f"{doc_hang_tram[hang_tram]} {doc_hang_chuc[hang_chuc]} {doc_hang_don_vi[hang_don_vi]}")