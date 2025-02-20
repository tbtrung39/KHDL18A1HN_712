def dinh_parabol(a, b, c):
    x_dinh = -b / (2 * a)
    y_dinh = a * x_dinh**2 + b * x_dinh + c
    return round(x_dinh, 2), round(y_dinh, 2)

a = float(input("Nhập hệ số a: "))
b = float(input("Nhập hệ số b: "))
c = float(input("Nhập hệ số c: "))

if a == 0:
    print("Đây không phải phương trình bậc 2.")
else:
    dinh = dinh_parabol(a, b, c)
    print(f"Tọa độ đỉnh của parabol là: {dinh}")
