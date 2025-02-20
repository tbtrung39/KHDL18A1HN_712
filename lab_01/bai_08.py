def tinh_trong_tam(A, B, C):
    x_G = (A[0] + B[0] + C[0]) / 3
    y_G = (A[1] + B[1] + C[1]) / 3
    return round(x_G, 2), round(y_G, 2)

Ax, Ay = map(float, input("Nhập tọa độ A (x y): ").split())
Bx, By = map(float, input("Nhập tọa độ B (x y): ").split())
Cx, Cy = map(float, input("Nhập tọa độ C (x y): ").split())

trong_tam = tinh_trong_tam((Ax, Ay), (Bx, By), (Cx, Cy))
print(f"Tọa độ trọng tâm của tam giác là: {trong_tam}")
