def X(n):
    if n == 0:
        return 1
    total = 0
    for i in range(n):
        total += (n - i)**2 * X(i)
    return total

n = int(input("Nhập n: "))
print(f"Giá trị X_{n} là:", X(n))
