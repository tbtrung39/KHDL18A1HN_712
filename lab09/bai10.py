def X(n):
    if n == 0:
        return 1
    return n**2 * X(n-1) + (n-1)**2 * X(n-2) + (n-2)**2 * X(n-3)

n = int(input("Nhập n: "))
print(f"X({n}) =", X(n))