# Nhập tọa độ của vector a
ax = float(input("Nhập tọa độ ax: "))
ay = float(input("Nhập tọa độ ay: "))
az = float(input("Nhập tọa độ az: "))

# Nhập tọa độ của vector b
bx = float(input("Nhập tọa độ bx: "))
by = float(input("Nhập tọa độ by: "))
bz = float(input("Nhập tọa độ bz: "))

# Tính tích vô hướng: a • b = ax * bx + ay * by + az * bz
dot_product = ax * bx + ay * by + az * bz

# Xuất kết quả
print(f"\nTích vô hướng của hai vector a và b là: {dot_product:.2f}")