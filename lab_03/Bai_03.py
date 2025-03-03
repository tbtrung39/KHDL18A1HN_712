n=int((input("nhap so nguyen duong n: ")))
if n<2:
    print("khong phai so nguyen to")
elif n==2:
    print("2 la so nguyen to")
else:
    for i in range(2,n):
        if n%i!=0:
            check=True
            break
        else:
            check=False
            break
    if check==True:
        print(n,"la so nguyen to")
    else:
        print(n,"khong phai so nguyen to")
