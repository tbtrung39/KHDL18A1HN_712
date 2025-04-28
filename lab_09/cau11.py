def double_factorial(n):
    if n <= 1:
        return 1
    return n * double_factorial(n-2)

n = int(input("Nhập n: "))
print(f"{n}!! =", double_factorial(n))