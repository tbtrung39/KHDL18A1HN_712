def permutation(n):
    if n == 1:
        return [[1]]
    result = []
    prev = permutation(n - 1)
    for p in prev:
        for i in range(len(p) + 1):
            new_p = p[:i] + [n] + p[i:]
            result.append(new_p)
    return result

n = int(input("Nhập n: "))
print("Tất cả các hoán vị của dãy 1 đến", n, "là:")
for p in permutation(n):
    print(p)
