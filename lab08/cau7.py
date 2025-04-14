def tinh_toan(a, b):
    return (a + b, a - b, a * b, a / b if b != 0 else "Không chia được")

a = float(input("Nhập số a: "))
b = float(input("Nhập số b: "))
tong, hieu, tich, thuong = tinh_toan(a, b)
print(f"Cộng: {tong}, Trừ: {hieu}, Nhân: {tich}, Chia: {thuong}")