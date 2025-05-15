n = int(input("Nhập n: "))
while n <= 0:
    n = int(input("Vui lòng nhập lại số nguyên dương n: "))

S = 0
for i in range(2, n + 2): 
    S += 1 / i
print(f"Tổng S = {S}")
S = 0
for i in range(2, n + 2):
    S += 1 / (i * (i + 1))
print(f"Tổng S = {S}")
S = 0
for i in range(2, n + 2):
    S += 1 / (i ** 0.5)
print(f"Tổng S = {S}")