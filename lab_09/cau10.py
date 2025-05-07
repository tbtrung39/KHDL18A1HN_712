def tinh_X(n):
    if n == 0:
        return 1
    tong = 0
    for i in range(n):
        tong += (n - i)**3 * tinh_X(i)
    return tong

n = int(input("Nhập n: "))
print(f"Giá trị X{n} là:", tinh_X(n))
