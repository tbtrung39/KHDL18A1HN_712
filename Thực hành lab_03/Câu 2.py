#Câu 2:
n=int(input("Nhập vào số n:"))
for i in range(1,n):
    tong_uoc=0
    for k in range(1,i):
        if i%k==0:
            tong_uoc+=k
    if tong_uoc==i:
        print(i)



