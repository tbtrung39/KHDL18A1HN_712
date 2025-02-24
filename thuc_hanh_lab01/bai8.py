Ax = float(input("Nhập tọa độ x của điểm A: "))
Ay = float(input("Nhập tọa độ y của điểm A: "))
Bx = float(input("Nhập tọa độ x của điểm B: "))
By = float(input("Nhập tọa độ y của điểm B: "))
Cx = float(input("Nhập tọa độ x của điểm C: "))
Cy = float(input("Nhập tọa độ y của điểm C: "))
Gx = (Ax + Bx + Cx) / 3
Gy = (Ay + By + Cy) / 3
print("Tọa độ trọng tâm của tam giác là:(", round(Gx, 2), ",", round(Gy, 2),")")
