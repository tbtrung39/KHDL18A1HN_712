n=input('nhap chuoi ky tu: ')
chuoi=''
for ky_tu in n:
    if '0'<=ky_tu<='9':
        chuoi+=ky_tu
if chuoi:
    print('chuoi so sau khi xu ly:',chuoi)
    so=int(chuoi)
    if so <=1:
        print('chuoi so khong phai la so hoan hao')
    else:
        tong_uoc=1
        for i in range(2,int(so**0.5)+1):
            if so %i==0:
                tong_uoc+=i + so//i
        if tong_uoc==so:
            print('chuoi so la chuoi hoan hao')
        else:
            print('chuoi so khong phai chuoi hoan hao')
else:
    print('chuoi khong chua so nao')
