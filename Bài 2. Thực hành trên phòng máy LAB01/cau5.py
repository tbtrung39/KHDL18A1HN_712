a = list(map(float, input("Nhập vector a (cách nhau bởi dấu cách): ").split()))
b = list(map(float, input("Nhập vector b (cách nhau bởi dấu cách): ").split()))

if len(a) != len(b):
    print("Hai vector phải có cùng số chiều!")
else:
    tich_vo_huong = sum(a[i] * b[i] for i in range(len(a)))
    print(f"Tích vô hướng của hai vector: {tich_vo_huong}")