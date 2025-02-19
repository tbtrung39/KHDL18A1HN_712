n = int(input("Nhập số chiều của vecto: "))
print("Nhập các thành phần của vecto a:")
a = []
for i in range(n):
    a.append(float(input(f"a[{i+1}]: ")))
print("Nhập các thành phần của vecto b:")
b = []
for i in range(n):
    b.append(float(input(f"b[{i+1}]: ")))
tich_vo_huong = 0
for i in range(n):
    tich_vo_huong += a[i] * b[i]
print(f"Tích vô hướng của vecto a và vecto b là: {tich_vo_huong}")
