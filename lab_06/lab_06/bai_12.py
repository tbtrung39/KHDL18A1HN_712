# Câu 12
sodu = 0  
while True:  
    nhatky = input("Nhap nhat ky giao dich: ").split()  
    if not nhatky:  
        break  
    try:  
        hd, tien = nhatky  
        tien = int(tien)  
        if hd == "D":  
            sodu += tien  
        elif hd == "W":  
            sodu -= tien  
        else:  
            print("Nhap sai loai giao dich. Vui long nhap 'D' hoac 'W'")  
    except ValueError:  
        print("Dinh dang nhap khong hop le. Vui long nhap dung dinh dang")  
print("So du cuoi cung la:", sodu)