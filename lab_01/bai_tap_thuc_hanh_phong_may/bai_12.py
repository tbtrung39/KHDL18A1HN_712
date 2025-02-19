import math

a = float(input("Nhập vận tốc ban đầu của xe: "))

t = (a**4) / (math.log(4, 5) + 1e-9)  # Tránh chia cho 0

print(f"Thời gian để xe dừng lại: {t:.2f} giây")

