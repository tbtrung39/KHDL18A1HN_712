def X(n):
    if n == 0:
        return 1
    s = 0
    for i in range(n):
        s += (n - i)**2 * X(i)
    return s

n = int(input("Nhập n: "))
print(f"X[{n}] =", X(n))