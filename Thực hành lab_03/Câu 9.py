#Câu 9:
n=int(input("Nhập số nguyên dương n:"))
if n<=0: print("Số không hợp lệ hãy nhập lại")
else:
    s4=0
    s5=0
    s6=0
#a)
    for i in range(1,n+1):
        s4+=i**2
        i+=1
    print(s4)
#b)
    for k in range(1,n+1):
        s5+=(2*k+1)**3
        k+=1
    print(s5)
#c)
    for j in range(2,n+1):
        s6+=(2*j)**4
        j+=1
    print(s6)
