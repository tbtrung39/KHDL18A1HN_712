n=int(input('Nhập n: '))
if n <=0:
    print('Vui lòng nhập lại!')
#a)
else:
    s4=0
    for i in range(1,n+1):
        s4+=i**2
    print('S4= ',s4)
#b)
n=int(input('Nhập n: '))
if n <=0:
    print('Vui lòng nhập lại!')
else:
    s5=0
    for j in range(1,n+1):
        s5+=(2*j+1)**3
    print('S5 =',s5)
#c
n=int(input('Nhập n: '))
if n <=0:
    print('Vui lòng nhập lại!')
else:
    s6=0
    for k in range(1,n+1):
        s6+=(2*k)**4
    print('S6 =',s6)
