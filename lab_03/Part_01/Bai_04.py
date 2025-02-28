n=int(input("Nhap n: "))
for a in range(2,n+1):
    s=0
    for i in range (1,a+1):
        if a%i==0:
            s+=1
    if s==2:
        print(a,"\n",end="")