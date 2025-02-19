a = float(input('Nhập hệ số a: '))
b = float(input('Nhập hệ số b: '))
c = float(input('Nhập hệ số c: '))
x_dinh = -b/(2*a)
y_dinh = a*x_dinh*x_dinh + b*x_dinh + c
print('Đỉnh cảu phương trinhg bậc 2 là: ',round(x_dinh,2),round(y_dinh,2))