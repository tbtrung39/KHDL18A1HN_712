while True:
    n=int(input("Nhap so nguyen duong n: "))
    if n > 0 :
        break
    print("n phai la so nguyen duong. Vui long nhap lai!")
S4 = 0
i = 1
while i <= n:
    S4 += i**2
    i += 1
print("S4 =", S4)
S5 = 0
i = 1
while i <= 2*n+1:
    S5 += i**3
    i +=2
print("S5 =", S5)
S6 = 0
i = 2
while i <= 2*n:
    S6 += 1**4
    i += 2
print("S6 =",S6)