# Câu 9.
#  a.
n = int(input("Nhập số nguyên dương n: "))
while n <= 0:
    n = int(input("Vui lòng nhập lại n (n phải lớn hơn 0): "))
S4 = 0
for i in range(1, n + 1):
    S4 += i ** 2
print(f"Tổng S4 = 1^2 + 2^2 + 3^2 + ... + n^2 = {S4}")

# b.
n = int(input("Nhập số nguyên dương n: "))
while n <= 0:
    n = int(input("Vui lòng nhập lại n (n phải lớn hơn 0): "))
S5 = 0
for i in range(1, n + 1):
    S5 += (2 * i - 1) ** 3
print(f"Tổng S5 = 1^3 + 3^3 + 5^3 + ... + (2n+1)^3 = {S5}")

# c.
n = int(input("Nhập số nguyên dương n: "))
while n <= 0:
    n = int(input("Vui lòng nhập lại n (n phải lớn hơn 0): "))
S6 = 0
for i in range(1, n + 1):
    S6 += (2 * i) ** 4
print(f"Tổng S6 = 2^4 + 4^4 + 6^4 + ... + (2n)^4 = {S6}")
