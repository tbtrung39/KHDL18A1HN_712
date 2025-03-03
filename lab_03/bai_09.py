n=int(input("nhap so nguyen n: "))
s4=0
for f in range (1,n+1):
    s4+=f**2
print("tong s4=",s4)

s5=0
for i in range (0,n+1):
    s5+=(2*i+1)**2
print("tong s5=",s5)

s6=0
for g in range (1,n+1):
    s6+=(2*n)**2
print("tong s6=",s6)