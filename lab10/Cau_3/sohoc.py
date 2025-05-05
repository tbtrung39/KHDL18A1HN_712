def Ucln(a,b):
    while b!=0:
        a,b=b,a%b
    return a
def Bcnn(a,b):
    return abs(a*b)//Ucln(a,b)
def SumDivisor(n):
    if n==0:
        return 0
    n=abs(n)
    t=0
    for i in range(1,n+1):
        if n%i==0:
            t+=i
    return t