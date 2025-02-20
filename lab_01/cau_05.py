a1, a2, a3 = map(float, input("Nhập các phần tử của vector a (cách nhau bởi dấu cách): ").split())
b1, b2, b3 = map(float, input("Nhập các phần tử của vector b (cách nhau bởi dấu cách): ").split())
tich_vo_huong = a1 * b1 + a2 * b2 + a3 * b3
print(f"Tích vô hướng của hai vector a và b là: {tich_vo_huong:.2f}")
