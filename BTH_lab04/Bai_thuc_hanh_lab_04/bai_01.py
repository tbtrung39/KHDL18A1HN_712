while True:
    n=int(input("Nhap n: "))
    if n>0:
        break
    print("Vui long nhap so nguyen duong!")
    
S4=0
i=1
while i<=n:
    S4+=i
    i+=1

S5=0
i=1
while i<=(2*n+1):
    S5+= i**3
    i+=2

S6=0
i=2
while i<=(2*n):
    S6 += i**4
    i+=2

print("s4= ",S4)
print("s5= ",S5)
print("s6= ",S6)