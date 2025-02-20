import random

def tinh_xac_suat(n):
    dem = 0
    for _ in range(n):
        x1, x2, x3 = random.randint(1, 6), random.randint(1, 6), random.randint(1, 6)
        if x1 == 6 and x2 == 6 and x3 == 6:
            dem += 1
    return round(dem / n, 2)

n = int(input("Nhập số lần tung xúc xắc: "))
xac_suat = tinh_xac_suat(n)
print(f"Xác suất có ít nhất 1 lần cả 3 xúc xắc ra 6 là: {xac_suat}")
