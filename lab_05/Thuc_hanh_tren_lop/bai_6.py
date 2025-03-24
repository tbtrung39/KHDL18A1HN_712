s=input("Nhap chuoi: ")
h="0123456789ABCDEFabcdef"
m=True
for x in s:
    if x not in h:
        m=False
        break
if m:
    d=0
    for x in s:
        if '0'<=x<='9':
            d=d*16+int(x)
        else:
            d=d*16 +(ord(x.upper())- ord('A')+10)
    print("La so Hex, gia tri thap phan:",d)
else:
    print("Khong phai so Hex")
