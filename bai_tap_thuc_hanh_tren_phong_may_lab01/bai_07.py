#Tính đỉnh của 1 phương trình bậc 2
print('Phương trình bậc 2: ax**2 + bx + c')
a=float(input('Nhập hệ số a: '))
b=float(input('Nhập hệ số b: '))
c=float(input('Nhập hệ số c: '))
x=-b/(2*a)
y=((4*a*c)-b**2)/(4*a)
print(f'Tọa độ đỉnh là: ({x},{y})')