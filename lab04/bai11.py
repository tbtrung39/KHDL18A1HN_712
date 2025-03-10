print("______________MENU DO UONG______________")
while True : 
    print("1.Cafe")
    print("2.Cam vat")
    print("3.Nuoc ep ca rot ")
    print("4.Nuoc loc ")
    print("5.Nuoc dua ")
    print("0.thoat menu ")
    luachon = int(input("Moi nhap lua chon do uong ")) 
    if luachon == 1 : 
        print("Ban da dat thanh cong cafe")
    elif luachon == 2 : 
        print("Ban da dat thanh cong cam vat ") 
    elif luachon == 3 : 
        print("Ban da dat thanh cong nuoc ep ca rot ") 
    elif luachon == 4 : 
        print("Ban da dat thanh cong nuoc loc ")
    elif luachon == 5 : 
        print("Ban da dat thanh cong nuoc dua ")
    elif luachon == 0 : 
        print("DA THOAT MENU")
        break 
    else :
        print("Lua chon sai vui long nhap lai ")