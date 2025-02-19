def doc_so_co_ba_chu_so(n):
    if not (100 <= n <= 999):
        return "Số không hợp lệ"

    don_vi = ["không", "một", "hai", "ba", "bốn", "năm", "sáu", "bảy", "tám", "chín"]
    chuc = ["", "mười", "hai mươi", "ba mươi", "bốn mươi", "năm mươi", "sáu mươi", "bảy mươi", "tám mươi", "chín mươi"]
    tram = ["", "một trăm", "hai trăm", "ba trăm", "bốn trăm", "năm trăm", "sáu trăm", "bảy trăm", "tám trăm", "chín trăm"]

    tram_n = n // 100
    chuc_n = (n % 100) // 10
    don_vi_n = n % 10

    if chuc_n == 0 and don_vi_n == 0:
        return tram[tram_n]
    elif chuc_n == 0:
        return f"{tram[tram_n]} {don_vi[don_vi_n]}"
    elif don_vi_n == 0:
        return f"{tram[tram_n]} {chuc[chuc_n]}"
    else:
        return f"{tram[tram_n]} {chuc[chuc_n]} {don_vi[don_vi_n]}"

n = int(input("Nhập số nguyên có ba chữ số: "))
print(doc_so_co_ba_chu_so(n))