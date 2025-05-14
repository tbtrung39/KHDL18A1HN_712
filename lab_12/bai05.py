def tổng_S1(n):
    if n == 1:
        return 1
    return n + tổng_S1(n - 1)

def tổng_S2(n):
    if n == 1:
        return 1
    return n * n + tổng_S2(n - 1)

try:
    n = int(input("Nhập số nguyên dương n: "))
    if n <= 0:
        raise ValueError("n phải là số nguyên dương.")

    print("S1 =", tổng_S1(n))
    print("S2 =", tổng_S2(n))
except ValueError as lỗi:
    print("Lỗi:", lỗi)