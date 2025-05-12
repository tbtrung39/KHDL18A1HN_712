def double_fact(n):
    if n == 0 or n == 1:
        return 1
    return n * double_fact(n - 2)

def tinh_S(k):
    if k == 1:
        return double_fact(1)
    return ((-1)**k) * double_fact(k) + tinh_S(k - 1)

k = int(input("Nhập k (k < 1000): "))
print("Giá trị của S là:", tinh_S(k))