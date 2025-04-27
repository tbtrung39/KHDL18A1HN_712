# Cau 11.
def giai_thua_kep(n):
    if n == 0 or n == 1:
        return 1
    return n * giai_thua_kep(n - 2)
def tong_gia_thua_kep(k):
    if k <= 1:
        return 0
    return giai_thua_kep(k-1) + tong_gia_thua_kep(k-1)
k = int(input("Nhap k (k< 1000): "))
print("Tong S la: ", tong_gia_thua_kep(k))