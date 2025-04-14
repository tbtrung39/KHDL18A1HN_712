def tinh_bieu_thuc(x, n):
    return x ** n

x = int(input("Nhập x: "))
n = int(input("Nhập n: "))
print(f"{x}^{n} =", tinh_bieu_thuc(x, n))
