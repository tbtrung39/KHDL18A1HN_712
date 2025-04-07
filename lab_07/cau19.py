nv = {}
n = int(input("nhap so luong nhan vien: "))
for  _ in range(n):
    ma_nv = input('ma nv: ')
    ho_ten = input('ho ten: ')
    nam_sinh = input('nam sinh: ')
    luong = input('luong: ')
    nv={'ho ten':ho_ten,'ma nhan vien':ma_nv,'nam sinh':nam_sinh,'luong':luong}
x=input('tim ma nhan vien: ')
print((nv.get(x,'khong tim thay nhan vien')))
y=input('ma nhan vien de tamg luong')
if y in nv:
    nv[y]['luong']+=1000000
z=input('ma nhan vien can xoa: ')
if z in nv:del nv[z]
sorted_nv=sorted(nv.items(),key=lambda x:x[1]['nam sinh'],reverse=True)
for ma_nv,info in sorted_nv:
    print(f'{ma_nv}:{info}')





