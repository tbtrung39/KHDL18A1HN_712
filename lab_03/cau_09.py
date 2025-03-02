while True:
    n = int(input("Nhập vào số nguyên dương n: "))
    if n > 0:
        break
    else:
        print("Vui lòng nhập số nguyên dương n > 0.")
S4 = 0
S5 = 0
S6 = 0
for i in range(1, n + 1):
    S4 += i ** 2
for i in range(1, n + 1):
    S5 += (2 * i - 1) ** 3
for i in range(1, n + 1):
    S6 += (2 * i) ** 4
print(f"Tổng S4 = 1^2 + 2^2 + ... + n^2 = {S4}")
print(f"Tổng S5 = 1^3 + 3^3 + 5^3 + ... + (2n+1)^3 = {S5}")
print(f"Tổng S6 = 2^4 + 4^4 + 6^4 + ... + (2n)^4 = {S6}")
