a = float(input("Nhập giá trị a: "))
b = float(input("Nhập giá trị b: "))
c = float(input("Nhập giá trị c: "))
if a == 0:
    print("Phương trình không phải là bậc hai.")
else:
    x_dinh = -b / (2 * a)
    y_dinh = a * x_dinh**2 + b * x_dinh + c
    x_dinh_rounded = round(x_dinh, 2)
    y_dinh_rounded = round(y_dinh, 2)
    print("Tọa độ đỉnh của parabol là: ({}, {})".format(x_dinh_rounded, y_dinh_rounded))
