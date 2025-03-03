n = int(input("Nhập n (số nguyên dương): "))

if n <= 0:
    print("n phải là số nguyên dương!")
else:
    s1 = n * (n + 1) // 2  # S1 = 1 + 2 + ... + n
    s2 = (n + 1) // 2 * (n + 1)  # S2 = 1 + 3 + 5 + ...
    s3 = (n + 1) * n  # S3 = 2 + 4 + 6 + ...

    print(f"S1 = {s1}")
    print(f"S2 = {s2}")
    print(f"S3 = {s3}")