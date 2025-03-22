# Nhập các hệ số a, b, c
a = float(input("Nhập hệ số a: "))
b = float(input("Nhập hệ số b: "))
c = float(input("Nhập hệ số c: "))

# Kiểm tra a khác 0 để đảm bảo là phương trình bậc 2
if a == 0:
    print("Đây không phải là phương trình bậc 2.")
else:
    # Tính tọa độ đỉnh
    x_dinh = -b / (2 * a)
    y_dinh = a * x_dinh**2 + b * x_dinh + c

    # Làm tròn đến hai chữ số thập phân
    x_dinh_rounded = round(x_dinh, 2)
    y_dinh_rounded = round(y_dinh, 2)

    # In kết quả
    print("Tọa độ đỉnh của phương trình là: ({}, {})".format(x_dinh_rounded, y_dinh_rounded))