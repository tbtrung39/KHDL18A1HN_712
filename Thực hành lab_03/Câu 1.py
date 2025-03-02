#Câu 1 :
n=int(input("Nhập vào số nguyên n:"))
tong = 1
tich = 1
for i in range(2,n+1):
    tich*=(2*(n+1))/(2*n+3)
    tong+=tich
print("%0.3f"%tong)
