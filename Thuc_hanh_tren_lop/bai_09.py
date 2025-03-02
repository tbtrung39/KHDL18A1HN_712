# Nhập số nguyên dương n
n = int(input("Nhập n: "))
while n <= 0:
    n = int(input("Nhập lại n (n > 0): "))

# Khởi tạo tổng các dãy số
S4 = 0
S5 = 0
S6 = 0

# Tính tổng bằng vòng lặp
for i in range(1, n+1):
    S4 += i**2  # Tổng bình phương
    S5 += i**3  # Tổng lập phương
    S6 += i**4  # Tổng lũy thừa bậc 4

# In kết quả
print(f"S4 = {S4}, S5 = {S5}, S6 = {S6}")