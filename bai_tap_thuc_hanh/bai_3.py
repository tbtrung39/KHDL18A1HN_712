r = float(input("Nhập bán kính đáy của hình trụ: "))
h = float(input("Nhập chiều cao của hình trụ: "))
sxq = 2*3.14*r*h
s2day = 2*3.14*r**2
stp = sxq + s2day
thetich = 3.14*r**2*h
print("Diện tích xung quanh của hình trụ là %0.2f"%sxq)
print("Diện tich toàn phần của hình trụ là %0.2f"%stp)
print("Thể tích của hình trụ là %0.2f"%thetich)