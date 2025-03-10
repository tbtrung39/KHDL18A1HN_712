n=input('nhap so nguyen duong: ')
so=['khong','mot','hai','ba','bon','nam','sau','bay','tam','chin','cham']
i=0
while i<=len(n):
    if n[i]=="0":
        print(so[0])
    elif n[i]=='1':
        print(so[1])
    elif n[i]=='2':
        print(so[2])
    elif n[i]=='3':
        print(so[3])
    elif n[i]=='4':
        print(so[4])
    elif n[i]=='5':
        print(so[5])
    elif n[i]=='6':
        print(so[6])
    elif n[i]=='7':
        print(so[7])
    elif n[i]=='8':
        print(so[8])
    elif n[i]=='9':
        print(so[9])
    elif n[i]=='.':
        print(so[10])
    i+=1
