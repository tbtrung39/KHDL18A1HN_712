def perm(n):
    if n == 1:
        return [[1]]
    perms = perm(n - 1)
    result = []
    for p in perms:
        for i in range(n):
            result.append(p[:i] + [n] + p[i:])
    return result

n = int(input())
for p in perm(n):
    print(p)
