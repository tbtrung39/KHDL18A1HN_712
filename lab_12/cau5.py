def tongS1(n):
    if n == 1: return 1
    return n + tongS1(n - 1)

def tongS2(n):
    if n == 1: return 1
    return n*n + tongS2(n - 1)

try:
    n = int(input("Nhập n: "))
    if n <= 0:
        raise ValueError("n phải là số nguyên dương")
    print("S1 =", tongS1(n))
    print("S2 =", tongS2(n))
except ValueError as e:
    print("Lỗi:", e)