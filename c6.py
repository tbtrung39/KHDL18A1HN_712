import random

def hoan_vi_ngau_nhien(A, result):
    if not A:
        print(result)
        return
    i = random.randint(0, len(A) - 1)
    result.append(A[i])
    A.pop(i)
    hoan_vi_ngau_nhien(A, result)

n = int(input("Nhập số nguyên n: "))
A = [i for i in range(1, n+1)]
result = []
hoan_vi_ngau_nhien(A, result)