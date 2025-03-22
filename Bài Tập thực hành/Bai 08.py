# Nhập tọa độ đỉnh A
print("Nhập tọa độ đỉnh A:")
x_a = float(input("x_a = "))
y_a = float(input("y_a = "))

# Nhập tọa độ đỉnh B
print("Nhập tọa độ đỉnh B:")
x_b = float(input("x_b = "))
y_b = float(input("y_b = "))

# Nhập tọa độ đỉnh C
print("Nhập tọa độ đỉnh C:")
x_c = float(input("x_c = "))
y_c = float(input("y_c = "))

# Tính tọa độ trọng tâm G
x_g = (x_a + x_b + x_c) / 3
y_g = (y_a + y_b + y_c) / 3

# Làm tròn x_g
x_g_100 = x_g * 100
x_g_int = int(x_g_100)
if x_g_100 - x_g_int >= 0.5:
    x_g_int += 1
x_g_rounded = x_g_int / 100

# Làm tròn y_g
y_g_100 = y_g * 100
y_g_int = int(y_g_100)
if y_g_100 - y_g_int >= 0.5:
    y_g_int += 1
y_g_rounded = y_g_int / 100

# In kết quả
print("Tọa độ trọng tâm G của tam giác là: (", end="")
print(x_g_rounded, end="")
print(", ", end="")
print(y_g_rounded, end="")
print(")")