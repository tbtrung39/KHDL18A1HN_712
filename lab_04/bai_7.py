
a = int(input("Nhap so nguyen thu nhat: "))
b = int(input("Nhap so nguyen thu hai: "))
x,y = a,b
while y!=0:
    x,y = y, x % y
bcnn = abs(a*b)//x
print(f"Bo chung nho nhat cua {a} va {b} la: {bcnn}")
