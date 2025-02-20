a = float(input("Nhập giá trị a: "))
b = float(input("Nhập giá trị b: "))
c = float(input("Nhập giá trị c: "))
x_dinh = -b / (2 * a)
y_dinh = a * (x_dinh ** 2) + b * x_dinh + c
print(f"Tọa độ đỉnh của phương trình bậc 2 là: ({x_dinh:.2f}, {y_dinh:.2f})")
