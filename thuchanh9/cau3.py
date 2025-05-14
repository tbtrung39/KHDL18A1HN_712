def pow_rec(a, n):
    if n == 0:
        return 1
    return a * pow_rec(a, n - 1)

a = int(input("Nhập số a: "))
n = int(input("Nhập số mũ n: "))

print(f"{a}^{n} = {pow_rec(a, n)}")
