n = int(input("Nhập n: "))
while n <= 0:
    n = int(input("Nhập lại n (phải là số nguyên dương): "))

S4 = 0
for i in range(1, n + 1):
    S4 += i ** 2
print("S4 =", S4)
