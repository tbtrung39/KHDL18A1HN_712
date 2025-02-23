x1, y1 = map(float, input("Nhập tọa độ đỉnh A (x1 y1): ").split())
x2, y2 = map(float, input("Nhập tọa độ đỉnh B (x2 y2): ").split())
x3, y3 = map(float, input("Nhập tọa độ đỉnh C (x3 y3): ").split())
Gx = (x1 + x2 + x3) / 3
Gy = (y1 + y2 + y3) / 3
print("Tọa độ trọng tâm của tam giác là:", round(Gx, 2), round(Gy, 2))