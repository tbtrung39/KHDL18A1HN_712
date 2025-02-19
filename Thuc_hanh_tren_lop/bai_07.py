# Nhập hệ số a, b, c
a = float(input("Nhập hệ số a: "))
b = float(input("Nhập hệ số b: "))
c = float(input("Nhập hệ số c: "))

# Tính tọa độ đỉnh của parabol y = ax^2 + bx + c
x_dinh = -b / (2 * a)
y_dinh = a * x_dinh**2 + b * x_dinh + c  # Tính giá trị y tại x_dinh

# Xuất kết quả, làm tròn đến 2 chữ số thập phân
print(f"\nTọa độ đỉnh của parabol là: ({x_dinh:.2f}, {y_dinh:.2f})")