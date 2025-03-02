n = int(input("Nhập n: "))
tong = 1
tu = 2
mau = 3

for i in range(n):
    tong += tu / mau
    tu += 2
    mau += 2

print(f"Kết quả: {tong:.3f}")