def giai_thua_kep(n):
    if n <= 1:
        return 1
    return n * giai_thua_kep(n - 2)

def tinh_tong(k):
    tong = 0
    for i in range(1, k + 1):
        tong += ((-1) ** i) * i * giai_thua_kep(i)
    return tong

n = int(input("Nhập giá trị n: "))
print(f"{n}!! =", giai_thua_kep(n))

k = int(input("Nhập k (<1000) để tính tổng S: "))
print("Tổng S là:", tinh_tong(k))

