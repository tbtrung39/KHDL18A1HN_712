def tich_vo_huong(a, b):
    return sum(a[i] * b[i] for i in range(len(a)))

n = int(input("Nhập số chiều của vector: "))

a = list(map(float, input("Nhập vector a: ").split()))
b = list(map(float, input("Nhập vector b: ").split()))

if len(a) != n or len(b) != n:
    print("Số phần tử không khớp với số chiều đã nhập.")
else:
    tich = tich_vo_huong(a, b)
    print(f"Tích vô hướng của hai vector: {tich}")
