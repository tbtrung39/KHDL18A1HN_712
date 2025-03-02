# Nhập n
n = int(input("Nhập n: "))
while n <= 0:
    n = int(input("Nhập lại n (n > 0): "))

tong = 0
for i in range(1, n+1):
    tong += i**3  # Cộng dồn tổng lập phương

# In kết quả
print(f"Tổng bậc 3 của {n} số nguyên đầu tiên là: {tong}")