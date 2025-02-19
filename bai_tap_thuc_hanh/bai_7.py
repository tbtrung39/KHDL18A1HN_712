a = float(input("Nhập giá trị a (hệ số bậc 2): "))
b = float(input("Nhập giá trị b (hệ số bậc 1): "))
c = float(input("Nhập giá trị c (hệ số tự do): "))
x_dinh = -b / (2 * a)
y_dinh = a * (x_dinh ** 2) + b * x_dinh + c
print("\nTọa độ đỉnh của phương trình bậc 2:")
print(f"X-đỉnh = {x_dinh}")
print(f"Y-đỉnh = {y_dinh}")