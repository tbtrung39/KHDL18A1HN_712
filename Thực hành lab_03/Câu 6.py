#Câu 6 :
n=int(input("Nhập số nguyên n: "))
tong=0
for i in range(1,n+1):
    tong+=i**3
print("Tổng bậc 3 của ",n," số nguyên đầu tiên là:",tong)