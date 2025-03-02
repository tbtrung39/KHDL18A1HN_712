while True:
    n = int(input("Nhập vào số nguyên dương n: "))
    if n > 0:
        break
    else:
        print("Vui lòng nhập số nguyên dương n > 0.")
S1 = n * (n + 1) / 2
S2 = (n + 1) ** 2
S3 = n * (n + 1)
print(f"Tổng S1 = 1 + 2 + 3 + ... + n = {S1}")
print(f"Tổng S2 = 1 + 3 + 5 + ... + (2n+1) = {S2}")
print(f"Tổng S3 = 2 + 4 + 6 + ... + 2n = {S3}")
