number = int(input("Nhập một số nguyên có ba chữ số: "))
if 100 <= abs(number) <= 999:
    hang_dv = ["", "một", "hai", "ba", "bốn", "năm", "sáu", "bảy", "tám", "chín"]
    hang_chuc   = ["", "mười", "hai mươi", "ba mươi", "bốn mươi", "năm mươi", "sáu mươi", "bảy mươi", "tám mươi", "chín mươi"]
    hang_tram  = ["", "một trăm", "hai trăm", "ba trăm", "bốn trăm", "năm trăm", "sáu trăm", "bảy trăm", "tám trăm", "chín trăm"]
    h = number // 100
    t = (number % 100) // 10
    u = number % 10
    result = hang_tram[h] 
    if t > 1:
        result += " " + hang_chuc[t]
        if u > 0:
            result += " " + hang_dv[u]
    elif t == 1:  
        if u > 0:
            result += " mười " + hang_dv[u]
        else:
            result += " mười"
    elif t == 0 and u > 0:  
        result += " lẻ " + hang_dv[u]

    print(f"Cách đọc số {number} là: {result}")
else:
    print("Số bạn nhập không phải là số nguyên có ba chữ số.")
