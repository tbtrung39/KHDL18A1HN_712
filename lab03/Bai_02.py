n=int(input('Nhap n: '))
print(f"cac so hoan hao nho hon {n} la: ")
for i in range(1,n):
    tonguoc=0
    for a in range(1,i):
        if i%a==0:
            tonguoc+=a
    if tonguoc==i:
        print(i,"\n",end="")
        