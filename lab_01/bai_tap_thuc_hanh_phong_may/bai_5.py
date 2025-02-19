a = list(map(float, input("Nhập tọa độ vector a (cách nhau bởi khoảng trắng): ").split()))
b = list(map(float, input("Nhập tọa độ vector b (cách nhau bởi khoảng trắng): ").split()))

tich_vo_huong = sum(a[i] * b[i] for i in range(len(a)))
print(f"Tích vô hướng của hai vector là: {tich_vo_huong:.2f}")
