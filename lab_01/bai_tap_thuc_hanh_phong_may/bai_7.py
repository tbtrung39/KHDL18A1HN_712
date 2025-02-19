a = float(input("Nhập hệ số a: "))
b = float(input("Nhập hệ số b: "))
c = float(input("Nhập hệ số c: "))

x_dinh = -b / (2 * a)
y_dinh = (-b**2 + 4 * a * c) / (4 * a)

print(f"Tọa độ đỉnh của phương trình bậc 2: ({x_dinh:.2f}, {y_dinh:.2f})")
