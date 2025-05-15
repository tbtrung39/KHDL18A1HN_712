def giai_thua_kep(n):
    if n == 0 or n == 1:
        return 1
    return n * giai_thua_kep(n - 2)
def tinh_S(k):
    tong = 0
    for i in range(1, k + 1):
        tong += ((-1) ** i) * giai_thua_kep(i)
    return tong
k = int(input("Nhập k (k < 1000): "))
if k < 1000:
    print(f"Tổng S = {tinh_S(k)}")
else:
    print("k phải nhỏ hơn 1000!")
