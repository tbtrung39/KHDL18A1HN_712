def giai_thua_kep(n):
    if n <= 1:
        return 1
    else:
        return n * giai_thua_kep(n - 2)

def tinh_S(k):
    tong = 0
    for i in range(1, k + 1):
        tong += ((-1) ** (i + 1)) * giai_thua_kep(i)
    return tong

print("Tổng S với k < 1000 là:")
print(tinh_S(999))

