# Nhập số chiều của vector
n = int(input("Nhập số chiều của vector: "))

# Nhập vector a
print("Nhập vector a:")
a = []
for i in range(n):
    gia_tri = float(input(f"a[{i}]: "))
    a.append(gia_tri)

# Nhập vector b
print("Nhập vector b:")
b = []
for i in range(n):
    gia_tri = float(input(f"b[{i}]: "))
    b.append(gia_tri)

# Tính tích vô hướng
tich_vo_huong = 0
for i in range(n):
    tich_vo_huong = tich_vo_huong + a[i] * b[i]

# In kết quả
print("Tích vô hướng của a và b là:", tich_vo_huong)
