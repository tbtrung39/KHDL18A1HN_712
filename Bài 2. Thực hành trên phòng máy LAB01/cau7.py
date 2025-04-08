a = float(input("Nhập a: "))
b = float(input("Nhập b: "))
c = float(input("Nhập c: "))

x_dinh = -b / (2 * a)
y_dinh = (4 * a * c - b**2) / (4 * a)

print(f"Tọa độ đỉnh của phương trình bậc 2: ({x_dinh:.2f}, {y_dinh:.2f})")