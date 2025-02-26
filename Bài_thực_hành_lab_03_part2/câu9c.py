n = int(input("Nhập n: "))
while n <= 0:
    n = int(input("Nhập lại n (phải là số nguyên dương): "))

S6 = 0
for i in range(n):
    S6 += (2 * i + 2) ** 4
print("S6 =", S6)