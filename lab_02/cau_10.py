t1=int(input("nhap luc bat dau thue: "))
t2=int(input("nhap luc ket thuc thue: "))
n=t2-t1
if t1<t2 and t1>=5 and t2<=22:
    if n<=3:
        d=n*100000
    if n>3 and n<11:
        d=3*100000+(n-3)*(100000*0.75)
    if n>=11 and n<=15:
        d=3*100000+(10)*(100000*0.75)+(n-10)*((100000*0.75)*0.9)
    print("so tien phai tra:",d)
else:
    print("nhap sai. vui long nhap lai")