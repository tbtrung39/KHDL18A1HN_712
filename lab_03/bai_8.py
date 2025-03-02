n = int(input("Nhập số nguyên dương n: "))
while n <= 0:
    print("Vui lòng nhập số nguyên dương!")
    n = int(input("Nhập số nguyên dương n: "))
S1 = n * (n + 1) // 2
S2 = (n + 1) ** 2
S3 = n * (n + 1)
print("Tổng S1 = %d" % S1)
print("Tổng S2 = %d" % S2)
print("Tổng S3 = %d" % S3)