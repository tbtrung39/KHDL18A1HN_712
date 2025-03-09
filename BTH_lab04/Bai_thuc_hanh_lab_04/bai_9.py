n=abs(int(input("Nhap n: ")))
s=0
while n>0:
    s+=n%10
    n//=10
print("Tong cac chu so: ",s)
