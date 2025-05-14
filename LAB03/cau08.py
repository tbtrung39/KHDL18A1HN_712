while True:
    n = int(input("Nhập n (n > 0): "))
    if n > 0:
        break
    print("Vui lòng nhập số nguyên dương!")
S1 = sum(i for i in range(1, n + 1))
S2 = sum(2 * i + 1 for i in range(n))
S3 = sum(2 * i for i in range(1, n + 1))
print(f"S1 = {S1}, S2 = {S2}, S3 = {S3}")
