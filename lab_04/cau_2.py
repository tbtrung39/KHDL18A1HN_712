n=int(input('nhap so n:'))
#a
s1=0
i=1
while i<=n:
    s1+=((-1)**(i+1))/(i)
    i=i+1
print(s1)
#b
s2=1/2
e=2
if n>=2:
    while e<=n:
        s2+=1/(e*(e+1))
        e+=1
    print(s2)
else:
    print('n khong dung dk')
#c
s3=0
g=2
if n>=2:
    while g<=n:
        s3+=1/((g)**0.5)
    print(s3)
else:
    print('nhap n sai dieu kien')
