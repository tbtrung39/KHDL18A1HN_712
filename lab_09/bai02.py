def ucln(a, b):
    if b == 0: return a
    return ucln(b, a % b)

def tinh_ucln(n):
    if n == 1:
        x = int(input("Nhập số: "))
        return x
    else:
        x = int(input("Nhập số: "))
        return ucln(x, tinh_ucln(n - 1))

n = int(input("Nhập số lượng số nguyên n: "))
print("Ước chung lớn nhất là:", tinh_ucln(n))

