so = int(input("Nhập vào số nguyên có ba chữ số: "))
if so > 999 : 
    print("Nhập sai vui lòng nhập lại : ")
else : 
    so_hang_tram = int(so/100)
    so_hang_chuc= int(so/10) % 10  
    so_don_vi = so % 10 
    print(f"{so_hang_tram} trăm {so_hang_chuc} mươi {so_don_vi}")
    if so_hang_chuc == 0 : 
        print(f"{so_hang_tram} trăm lẻ {so_don_vi}")
    elif so_don_vi == 0 : 
        print(f"{so_hang_tram} trăm {so_hang_chuc} mươi")