#Câu 11:
số_container = input("Nhập số container: ")
if len(số_container) != 10:
    print("Lỗi")
else:
    tổng_trọng_số = 0  
    chữ_cái = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"  
    giá_trị_bắt_đầu = 10  
    for vị_trí in range(len(số_container)):
        ký_tự = số_container[vị_trí]
        if 'A' <= ký_tự <= 'Z':  
            giá_trị = giá_trị_bắt_đầu
            for chữ in chữ_cái:
                if chữ == ký_tự:
                    break
                giá_trị += 1
                if giá_trị % 11 == 0:  
                    giá_trị += 1
        elif '0' <= ký_tự <= '9': 
            giá_trị = int(ký_tự)
        else:  
            print("Lỗi")
            break  
        tổng_trọng_số += giá_trị * (2 ** vị_trí)
    else:  
        số_kiểm_tra = tổng_trọng_số % 11
        print("Số kiểm tra tính được:", số_kiểm_tra)
