n = int(input("Nhập một số nguyên dương: "))
while n <= 0:
    print("Vui lòng nhập số nguyên dương!")
    n = int(input("Nhập lại: "))
S4 = 0
S5 = 0
S6 = 0

for i in range(1, n + 1):
    S4 += i ** 2
    S5 += (2 * i - 1) ** 3
    S6 += (2 * i) ** 4 
print(f"S4 = {S4}")
print(f"S5 = {S5}")
print(f"S6 = {S6}")
