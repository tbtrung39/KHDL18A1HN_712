#Câu 11:
a=input("Nhap danh sach a: ")
a=a.split()
for i in range(len(a)):
    a[i] = int(a[i])
print("Danh sach a: ",a)
 
b=[]
for x in a:
    if x%3==0 and x%5 !=0:
        b.append(x)
print("Ds chia het cho 3 nhung khong hcia het cho 5 la: ",b)

c=[]
for x in a:
    c.append(x**2)
    print("Ds binh phuong cac phan tu cua a: ",c)