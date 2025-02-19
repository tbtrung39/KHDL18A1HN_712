print('Nhập a1,b1,c1:')
a1 = float(input('a1='))
b1 = float(input('b1='))
c1 = float(input('c1='))
print('Nhập a2,b2,c2:')
a2 = float(input('a2='))  # Sửa lỗi chính tả ở đây
b2 = float(input('b2='))  # Sửa lỗi chính tả ở đây
c2 = float(input('c2='))  # Sửa lỗi chính tả ở đây

# Tính định thức d, dx, dy
d = a1 * b2 - a2 * b1
dx = c1 * b2 - c2 * b1
dy = a1 * c2 - a2 * c1

if d != 0:
    print('Phương trình có nghiệm duy nhất x=%0.2f và y=%0.2f' % ((dx / d), (dy / d)))
else:
    if dx == 0 and dy == 0:
        print("Vô số nghiệm (Vô định)")
    else:
        print("Vô nghiệm.")