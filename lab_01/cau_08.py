x1, y1 = map(float, input("Nhập tọa độ của đỉnh A ").split()) 
x2, y2 = map(float, input("Nhập tọa độ của đỉnh B ").split())
x3, y3 = map(float, input("Nhập tọa độ của đỉnh C ").split())
xg = (x1 + x2 + x3) / 3 
yg = (y1 + y2 + y3) / 3 
print(f"Tọa độ trọng tâm của tam giác là: ({xg}, {yg})") 