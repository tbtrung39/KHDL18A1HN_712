def luy_thua(a, n):
    if n == 0:
        return 1
    else:
        return a * luy_thua(a, n - 1)

a = int(input("Nhập số a: "))
n = int(input("Nhập số mũ n: "))

print(f"{a}^{n} =", luy_thua(a, n))
