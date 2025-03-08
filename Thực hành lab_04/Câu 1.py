#Câu 1:
n=int(input("Nhập vào số nguyên dương n:"))
while n<0:
    n=int(input("Hãy nhập lại số nguyên dương n:"))
#a)
s4=0
i=1
while i<=n:
    s4+=i**2
    i+=1
print(s4)
#b)
s5=0
i=1
while i<=n:
    s4+=i**2
    i+=1
print(s4)
#b)
s5=0
j=1
while j<=n:
    s5+=(2*n+1)**3
    j+=1
print(s5)
#c)
s6=0
k=1
while k<=n:
    s6+=(2*n)**4
    k+=1
print(s6)