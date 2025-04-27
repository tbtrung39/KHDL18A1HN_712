# Cau 5.
def permutation(n):
    if n == 1:
        return [[1]]
    prev = permutation(n - 1)
    result = []
    for p in prev:
        for i in range(len(p) + 1):
            result.append(p[:i] + [n] + p[i:])
    return result

n = int(input("Nhập n: "))
res = permutation(n)
for p in res:
    print(p)