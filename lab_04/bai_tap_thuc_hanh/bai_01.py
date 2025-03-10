# Cau 1.
while True:
    n = int(input("Nhập số nguyên dương n: "))
    if n > 0:
        break
    print("Vui lòng nhập số nguyên dương lớn hơn 0!")
# Tính S4 = 1^2 + 2^2 + 3^2 + ... + n^2
S4 = 0
i = 1
while i <= n:
    S4 += i ** 2
    i += 1
print("Tổng S4 =", S4)
# Tính S5 = 1^3 + 3^3 + 5^3 + ... + (2n+1)^3
S5 = 0
i = 1
while i <= (2 * n + 1):
    S5 += i ** 3
    i += 2
print("Tổng S5 =", S5)
# Tính S6 = 2^4 + 4^4 + 6^4 + ... + (2n)^4
S6 = 0
i = 2
while i <= (2 * n):
    S6 += i ** 4
    i += 2
print("Tổng S6 =", S6)