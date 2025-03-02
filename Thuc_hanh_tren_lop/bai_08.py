# Nhập số nguyên dương n
n = int(input("Nhập n: "))
while n <= 0:
    n = int(input("Nhập lại n (n > 0): "))

# Tính các tổng theo công thức
S1 = n * (n + 1) // 2
S2 = (n + 1) // 2
S3 = n * (n + 1)

# In kết quả
print(f"S1 = {S1}, S2 = {S2}, S3 = {S3}")