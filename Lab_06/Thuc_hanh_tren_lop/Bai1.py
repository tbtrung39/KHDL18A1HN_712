a=[2,-4,1,9,-3,6,-3,-2,6,8]

tong=0
for x in a:
    tong+=x
print("Tong: ",tong)

duong=0
tongduong=0
for x in a: 
    if x>0:
        duong+=1
        tongduong+=duong
print("so luong so duong: ",duong)
print("Tong cac so duong: ",tongduong)

va1=-1
for i in range(len(a)):
    if a[i] <0:
        va1=i
print("Vi tri cua phan tu am dau tien la: ",va1)

vdc = -1
for i in range(len(a) -1,-1,-1):
    if a[i]>0:
        vdc=i
        break
print("Vi tri cua phan tu duong cuoi cung la: ",vdc)

max=a[0]
vitrimax=0
for i in range(len(a)):
    if a[i] >= max:
        max=a[i]
        vitrimax=i
print("Phan tu lon nhat: ",max)
print("Vi tri cua phan tu lon nhat ",vitrimax)