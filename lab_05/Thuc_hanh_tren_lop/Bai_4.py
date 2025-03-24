a=input("Nhap chuoi 1: ")
b=input("Nhap chuoi 2: ")
c=""
i=0
while i< len(a) and i<len(b):
    c+= a[i] +b[i]
    i+=1
c += a[i:] 
c += b[i:]
print("Chuoi sau khi tron: ",c)