# Nhập số nguyên dương n
n = int(input("Nhập n: "))
while n <= 0:
    n = int(input("Nhập lại n (n > 0): "))

# Khởi tạo tổng S
S = 0
for i in range(1, n+1):
    S += 1/i  # Cộng dồn nghịch đảo

# In kết quả
print(f"Tổng nghịch đảo của {n} số đầu tiên: {S}")