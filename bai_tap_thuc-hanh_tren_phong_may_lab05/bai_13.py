a=input('nhap chuoi A chi chua cac chu so')
b=input('nhap chuoi B chi chua cac chu so')
check=False
for i in range(1,len(a)):
    c=a[:1]
    d=a[1:]
    for j in range(1,len(b)):
        e=b[:j]
        f=b[1:]
        if int(c)+int(d)==int(e)+int(f):
            print(f'{c}+{d}={e}+{f}')
            check=True
            break
    if check:
        break
if not check:
    print('khong ton tai cach dat')