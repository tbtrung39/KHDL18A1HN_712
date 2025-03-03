#a)
n=int(input('Nhập n: '))
if n <=0:
    print('Vui lòng nhập lại!')
else:
    s = 0
    for i in range(1,n+1):
        s+=i
    print('S1 = ',s)
#b)
n=int(input('Nhập n: '))
if n <=0:
    print('Vui lòng nhập lại!')
else:
    s2 = 0
    for i in range(1,n+1,2):
        s2+=i
    print('S2 =',s2)
#c)
n=int(input('Nhập n: '))
if n <=0:
    print('Vui lòng nhập lại!')
else:
    s3=0
    for i in range(2,n+1,2):
        s3+=i
    print('S3 =',s3)




