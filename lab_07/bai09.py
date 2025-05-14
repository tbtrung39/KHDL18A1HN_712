n = int(input("Nhập số tự nhiên n: "))
tap_A = {i for i in range(1, n+1) if n % i == 0}
tap_B = {i for i in range(1, n+1) if n % i != 0}
print("Tập hợp A (ước của n):", tap_A)
print("Tập hợp B (không là ước của n):", tap_B)