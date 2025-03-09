n = int(input("Nhập n: "))
while n <= 0:
    n = int(input("Vui lòng nhập lại số nguyên dương n: "))

S = 0
for i in range(2, n + 2):  # Bắt đầu từ 2 đến n+1
    S += 1 / i
print(f"Tổng S = {S}")

# b) S = 1/(2.3) + 1/(3.4) + 1/(4.5) + ...
S = 0
for i in range(2, n + 2):
    S += 1 / (i * (i + 1))
print(f"Tổng S = {S}")

# c) S = 1/√2 + 1/√3 + 1/√4 + ...
S = 0
for i in range(2, n + 2):
    S += 1 / (i ** 0.5)
print(f"Tổng S = {S}")