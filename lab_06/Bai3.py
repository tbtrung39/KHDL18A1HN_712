a=[]
while True:
    num=int(input("Nhap so (0 de ket thuc nhap):"))
    if num==0:
        break
    a.append(num)
print("Danh sach ban dau: ",a)
dsduong=[]
dskhac=[]
for x in a:
    if x>0:
        dsduong.append(x)
    else:
        dskhac.append(x)
a=dsduong+dskhac
print("Danh sach sau khi chuyen so duong len dau: ",a)
m=int(input("Nhap so m de chen vao danh sach: "))
a.insert(0,m)
a.append(m)
if len(a)>=5:
    a.insert(4,m)
print("Danh sach sau khi chen so m: ",a)