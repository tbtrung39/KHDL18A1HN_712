#Câu 8 :
n=int(input("Nhập vào số nguyên dương n:"))
if n<=0: print("Số không hợp lệ hãy nhập lại")
else:
    S1=n*(n+1)//2
    S2=(n+1)*2
    S3=n*(n+1)
print("Tổng S1,S2,S3 lần lượt là:",S1,S2,S3)
