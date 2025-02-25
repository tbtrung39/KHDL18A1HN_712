n=float(input("nhap diem trung binh: "))
if n>=0 or n<=10:
    if n>=0 or n<=3:
        print("thuoc loai kem")
    elif n>3 or n<=4:
        print("thuoc loai yeu")
    elif n>4 or n<=6:
        print("thuoc loai trung binh")
    elif n>6 or n<8:
        print("thuoc loai kha")
    else:
        print("thuoc loai gioi")
else:
    print("nhap sai. vui long nhap lai")