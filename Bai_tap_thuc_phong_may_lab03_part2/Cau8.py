# Cau 8.
# a.
n = int(input("Nhập số nguyên dương n: "))
while n <= 0:
    n = int(input("Vui lòng nhập lại n (n phải lớn hơn 0): "))
S1 = n * (n + 1) // 2  
print(f"Tổng S1 = 1 + 2 + 3 + ... + n = {S1}")

# b.
n = int(input("Nhập số nguyên dương n: "))
while n <= 0:
    n = int(input("Vui lòng nhập lại n (n phải lớn hơn 0): "))
S2 = (n + 1) ** 2 
print(f"Tổng S2 = 1 + 3 + 5 + ... + (2n+1) = {S2}")

# c.
n = int(input("Nhập số nguyên dương n: "))
while n <= 0:
    n = int(input("Vui lòng nhập lại n (n phải lớn hơn 0): "))
S3 = n * (n + 1)
print(f"Tổng S3 = 2 + 4 + 6 + ... + 2n = {S3}")
