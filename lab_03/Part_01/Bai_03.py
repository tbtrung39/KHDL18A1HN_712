n=int(input("Nhap n: "))
t=0
for i in range(1,n+1):
    if n%i==0:
        t=1
if t==2:
    print(n,' la so nguyen to')
else:
    print(n,' khong phai la so nguyen to')
    duoi=n-1
    for duoi in range(n-1,1,-1):
        t=0
        for i in range(1, duoi+1):
            if duoi%i==0:
                t+=1
        if t==2:
            break
    tren=n+1
    for tren in range(n+1, 100000000):
        t=0
        for i in range(1, tren+1):
            if tren%i==0:
                t+=1
        if t==2:
            break
    if n-duoi<=tren-n:
        print(f"snt gan nhat la {duoi}")
    else:
        print(f"snt gan nhat la {tren}")

