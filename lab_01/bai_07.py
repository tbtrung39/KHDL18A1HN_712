a = float(input('a = '))
b = float(input('b = '))
c = float(input('c = '))
x_dinh = -b/(2*a)
y_dinh = a*(x_dinh**2) + b*x_dinh + c
print(f'Tọa độ đỉnh của phương trình là: ({round(x_dinh,2)}, {round(y_dinh, 2)})')