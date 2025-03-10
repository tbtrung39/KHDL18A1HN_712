n = int(input("Nhập số nguyên dương n: "))
while n <= 0:
    n = int(input("Vui lòng nhập lại n: "))
# Câu a
S_a = 0
sign = 1
for i in range(1, n + 1):
    S_a += sign * (1 / i)
    sign *= -1
print("S_a =", S_a)

# Câu b
S_b = 0
for i in range(2, n + 2):
    S_b += 1 / (i * (i - 1))
print("S_b =", S_b)

# Câu c
import math
S_c = 0
for i in range(2, n + 2):
    S_c += 1 / math.sqrt(i)
print("S_c =", S_c)
