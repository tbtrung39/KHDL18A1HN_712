n = int(input("Nhập n: "))
while n <= 0:
    n = int(input("Nhập lại n (n > 0): "))
S1 = n * (n + 1) // 2
print("S1 =", S1)
