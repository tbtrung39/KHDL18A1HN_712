xA = float(input("Nhập tọa độ x của đỉnh A: "))
yA = float(input("Nhập tọa độ y của đỉnh A: "))
xB = float(input("Nhập tọa độ x của đỉnh B: "))
yB = float(input("Nhập tọa độ y của đỉnh B: "))
xC = float(input("Nhập tọa độ x của đỉnh C: "))
yC = float(input("Nhập tọa độ y của đỉnh C: "))
x_trong_tam = (xA + xB + xC) / 3
y_trong_tam = (yA + yB + yC) / 3
print("Tọa độ trọng tâm của tam giác là: ({:.2f}, {:.2f})".format(x_trong_tam, y_trong_tam))