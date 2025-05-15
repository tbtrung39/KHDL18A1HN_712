def tinh_X(n, cache=None):
    if cache is None:
        cache = {}
    if n in cache:
        return cache[n]
    if n == 0:
        return 1
    tong = 0
    for i in range(n):
        tong += (n - i) ** 2 * tinh_X(i, cache)
    cache[n] = tong
    return tong
n = int(input("Nhập n: "))
print(f"X_{n} =", tinh_X(n))
