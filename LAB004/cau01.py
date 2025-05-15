n = int(input("Nhập số nguyên dương n: "))
while n <= 0:
    n = int(input("Vui lòng nhập lại số nguyên dương n: "))

S4 = sum(i**2 for i in range(1, n+1))
S5 = sum((2*i - 1)**3 for i in range(1, n+1))
S6 = sum((2*i)**4 for i in range(1, n+1))

print(f"S4 = {S4}")
print(f"S5 = {S5}")
print(f"S6 = {S6}")
