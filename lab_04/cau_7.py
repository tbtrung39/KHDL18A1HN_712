a=int(input("nhap so thu nhat: "))
b=int(input("Nhap so thu 2: "))
x=abs(a)
y=abs(b)
while y:
    x,y=y, x%y
    bcnn= abs(a*b) // x
print(bcnn)