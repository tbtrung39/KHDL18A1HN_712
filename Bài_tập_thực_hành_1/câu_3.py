r = float(input('nhập bán kính hình trụ: '))
h = float(input('nhập chiều cao hình trụ: '))
sxq = 2*3.14*r*h
stp = 2*3.14*r*(r+h)
v = 3.14*r**2*h
print('diện tích xung quanh hình trụ là: ', sxq)
print('diện tích toàn phần hình trụ là: ', stp)
print('thể tích hình trụ là', v)