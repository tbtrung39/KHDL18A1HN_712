while True:
    n = int(input("Nhập n (n > 0): "))
    if n > 0:
        break
    print("Vui lòng nhập số nguyên dương!")
S4 = sum(i ** 2 for i in range(1, n + 1))
S5 = sum((2 * i + 1) ** 3 for i in range(n))
S6 = sum((2 * i) ** 4 for i in range(1, n + 1))
print(f"S4 = {S4}, S5 = {S5}, S6 = {S6}")
