n=int(input("nhap so nguyen to co 3 chu so: "))
if n < 100 or n > 999:
    print("Số không có ba chữ số!")
else:
    o_list = ["", "một", "hai", "ba", "bốn", "năm", "sáu", "bảy", "tám", "chín"]
    t_list = ["", "mười", "hai mươi", "ba mươi", "bốn mươi", "năm mươi", "sáu mươi", "bảy mươi", "tám mươi", "chín mươi"]
    h_list = ["", "một trăm", "hai trăm", "ba trăm", "bốn trăm", "năm trăm", "sáu trăm", "bảy trăm", "tám trăm", "chín trăm"]
    h = n // 100
    t = (n // 10) % 10
    o = n % 10
    if t!=0:
        if t == 0 and o == 0:
            print(h_list[h])  
        elif t == 1 and o == 0:
            print(h_list[h] + " mười")
        elif t == 1:
            print(h_list[h] + " mười " + o_list[o])  
        else:
            print(h_list[h] + " " + t_list[t] + " " + o_list[o])
    elif t==0 and h!=0 and o!=0:
        print(h_list[h] + " "+ "linh"+ " "+ o_list[o])