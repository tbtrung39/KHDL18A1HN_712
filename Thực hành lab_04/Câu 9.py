#Câu 9:
n=int(input("Nhập vào số nguyên dương:"))
while n<0:
    n=int(input("Hãy nhập số nguyên dương:"))
tong=0
while n>0:
    tong+=n%10
    n//=10
print("Tổng các chữ số:",tong)