n = int(input("nhập n = "))
S1 = S2 = S3 = 0

for i in range(1, n + 1):
    S1 += i ** 2

for i in range(1, n + 1, 2):
    S2 += i ** 3

for i in range(2, n * 2 + 1, 2):
    S3 += i ** 4

print("S1 =", S1)
print("S2 =", S2)
print("S3 =", S3)