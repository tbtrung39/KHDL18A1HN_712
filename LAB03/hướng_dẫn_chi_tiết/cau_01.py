n = int(input("Nhập n: "))
sum_result = 0.0

for i in range(1, n + 1):
    sum_result += (2 * i + 1) / (2 * i + 3)

print(f"Kết quả: {sum_result:.3f}")