a=float(input("nhap he so a="))
b=float(input("nhap he so b="))
c=float(input("nhap he so c="))
delta=b**2-4*a*c
if delta<0:
    print("phuong trinh vo nghiem")
elif delta==0:
    print("phuong trinh co nghiem kep x1=x2=%0.2f"%-b/2*a)
else:
    x1=(-b-delta**1/2)/2*a
    x2=(-b+delta**1/2)/2*a
    print("phuong trinh co hai nghiem phan biet la: x1=%0.2f"%x1,"va x2=%0.2f"%x2)