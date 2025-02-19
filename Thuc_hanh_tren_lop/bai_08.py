def centroid(x1, y1, x2, y2, x3, y3):
 xg = (x1 + x2 + x3) / 3
 yg = (y1 + y2 + y3) / 3
 return round(xg, 2), round(yg, 2)
x1, y1 = map(float, input("Nhập tọa độ A (x1, y1): ").split())
x2, y2 = map(float, input("Nhập tọa độ B (x2, y2): ").split())
x3, y3 = map(float, input("Nhập tọa độ C (x3, y3): ").split())
G = centroid(x1, y1, x2, y2, x3, y3)
print(f"Trọng tâm tam giác: ({G[0]}, {G[1]})")