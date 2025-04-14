def tinh_toan(a, b):
    return a + b, a - b, a * b, a / b if b != 0 else "Không chia được cho 0"

a = float(input("Nhập a: "))
b = float(input("Nhập b: "))
cong, tru, nhan, chia = tinh_toan(a, b)
print("Tổng:", cong)
print("Hiệu:", tru)
print("Tích:", nhan)
print("Thương:", chia)
