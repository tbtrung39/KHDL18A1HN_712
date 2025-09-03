import math
x=float(input("NHap x(radian): "))
s, t, n= 0,1,0
while abs(t)> 1e-4:
    s+=t
    n+=1
    t*= -x**2 / (2*n * (2*n-1))
print(f"Gia tri xap xi cua cos(x) la {s}")
print(f"gia tri thuc te cua cos(x) la {math.cos(x)}")