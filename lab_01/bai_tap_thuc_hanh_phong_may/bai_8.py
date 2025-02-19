x1, y1 = map(float, input("Nhập tọa độ điểm A: ").split())
x2, y2 = map(float, input("Nhập tọa độ điểm B: ").split())
x3, y3 = map(float, input("Nhập tọa độ điểm C: ").split())

x_trong_tam = (x1 + x2 + x3) / 3
y_trong_tam = (y1 + y2 + y3) / 3

print(f"Tọa độ trọng tâm của tam giác là: ({x_trong_tam:.2f}, {y_trong_tam:.2f})")
