#Câu 7:
a=int(input("Nhập số nguyên a:"))
b=int(input("Nhập số nguyên b:"))
while a<=0 or b<=0:
    print("Hãy nhập lại 2 số nguyên dương")
    a=int(input("Nhập số nguyên a:"))
    b=int(input("Nhập số nguyên b:"))
x,y=a,b
while y!=0:
    x,y=y,x%y
bcnn=abs(a*b)//x
print("Bội chung nhỏ nhất của", a, "và", b, "là", bcnn)
