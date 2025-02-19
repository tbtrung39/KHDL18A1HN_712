pi = 3.14
r = float(input('Nhập bán kính: '))
h = float(input('Nhập chiều cao: '))
Sxq = 2*pi*r*h
print('Diện tích xung quanh của khối trụ là:',round(Sxq,2))
Stp = Sxq + 2*pi*r*r
print('Diện tích toàn phần của khối trụ là: ',round(Stp,2))
V = pi*r*r*h
print('Thể tích của khối trụ là: ',round(V,2))