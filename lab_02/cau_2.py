a,b,c=map(int,input("nhap he so cua phuong trinh bac 2: ").split())
delta=b**2-4*a*c
if delta <0:
    print("phuong trinh vo nghiem")
elif delta==0:
    print("phuong trinh co mot nghiem duy nhat la: %0.2f"%-b/2*a)
else:
    print("phuong trinh co hai nghiem la: x1=%0.2f"%(-b-delta**1/2)/2*a,"va x2=%0.2f"%(-b+delta**1/2)/2*a)

