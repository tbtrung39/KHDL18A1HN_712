#câu a
n = int(input("Nhập số nguyên dương n: "))
if n <= 0:
    print("Vui lòng nhập một số nguyên dương lớn hơn 0.")
    n = int(input("Nhập số nguyên dương n: "))
S1 = n * (n + 1) // 2  
print(f"Tổng S1 (1 + 2 + 3 + ... + n) là: {S1}")

#câu b
n = int(input("Nhập số nguyên dương n: "))
if n <= 0:
    print("Vui lòng nhập một số nguyên dương lớn hơn 0.")
    n = int(input("Nhập số nguyên dương n: "))
S2 = (n + 1) ** 2
print(f"Tổng S2 (1 + 3 + 5 + ... + (2n+1)) là: {S2}")


#câu c
n = int(input("Nhập số nguyên dương n: "))
if n <= 0:
    print("Vui lòng nhập một số nguyên dương lớn hơn 0.")
    n = int(input("Nhập số nguyên dương n: "))
S3 = n * (n + 1)
print(f"Tổng S3 (2 + 4 + 6 + ... + 2n) là: {S3}")


