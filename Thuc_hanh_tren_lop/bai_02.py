# a) 1 + 1/2 + 1/3 + ... + 1/n
n = int(input("Nhập số nguyên dương n: "))
S1 = 0
i = 1
while i <= n:
    S1 += 1 / i
    i += 1
print("Tổng S1:", S1)

# b) 1 / (1.2) + 1 / (2.3) + 1 / (3.4) + ...
S2 = 0
i = 1
while i <= n:
    S2 += 1 / (i * (i + 1))
    i += 1
print("Tổng S2:", S2)

# c) 1 / √1 + 1 / √2 + 1 / √3 + ...
S3 = 0
i = 1
while i <= n:
    S3 += 1 / (i ** 0.5)
    i += 1
print("Tổng S3:", S3)