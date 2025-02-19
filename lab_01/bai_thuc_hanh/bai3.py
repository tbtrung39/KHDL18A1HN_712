h = float(input("Nhập chiều cao: "))
r = float(input("Nhập bán kính: "))
pi = 3.14
sxq = 2*pi*r*h
stp = sxq +2*pi*(r*r)
v = pi *(r*r) *h 
print("Diện tích xung quanh khối trụ là :",sxq)
print("Diện tích toàn phần khối trụ là :",stp)
print("Thể tích của khối trụ là :",v)