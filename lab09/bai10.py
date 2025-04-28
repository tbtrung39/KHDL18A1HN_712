def X(n):
    if n==0 :
        return 1 
    total = 0 
    for k in range(n):
        total +=(n-k)**2* X(k)
    return total 
n=int(input("Nhap n:"))
print(f"X_{n}",X(n))