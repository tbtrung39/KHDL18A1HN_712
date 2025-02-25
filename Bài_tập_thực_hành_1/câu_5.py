n = int(input("Nhập số chiều của vector a: "))
a = []
for i in range(n):
    a.append(float(input(f"Nhập phần tử thứ {i+1} của vector a: ")))
b = []
for i in range(n):
    b.append(float(input(f"Nhập phần tử thứ {i+1} của vector b: ")))
tich_vo_huong = 0
for i in range(n):
    tich_vo_huong += a[i] * b[i]
print("Tích vô hướng của vector a và vector b là:", tich_vo_huong)