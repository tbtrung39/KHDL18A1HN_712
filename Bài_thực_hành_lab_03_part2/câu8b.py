n = int(input("Nhập n: "))
while n <= 0:
    n = int(input("Nhập lại n (phải là số nguyên dương): "))

S2 = 0
for i in range(n + 1):
    S2 += (2 * i + 1)

print("S2 =", S2)