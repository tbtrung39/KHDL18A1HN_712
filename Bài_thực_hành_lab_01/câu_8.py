x1 , y1 = map(float, input("Nhập tọa độ A(x1,y1):").split())
x2 , y2 = map(float, input("Nhập tọa độ B(x2,y2):").split())
x3 , y3 = map(float, input("Nhập tọa độ C(x3,y3):").split())
x = (x1 + x2 + x3)/3
y = (y1 + y2 + y3)/3
x_trong_tam = '%0.2f'%(x)
y_trong_tam = '%0.2f'%(y)
print("tọa độ trọng tâm tam giác là: (",x_trong_tam,",",y_trong_tam,")")