n = int(input("Nhập n: "))
while n <= 0:
    n = int(input("Nhập lại n (n > 0): "))

S3 = n * (n + 1)
print("S3 =", S3)