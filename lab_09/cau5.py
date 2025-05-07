def permutation(n):
    if n == 1:
        return [[1]]
    
    ket_qua = []
    for p in permutation(n - 1):
        for i in range(len(p) + 1):
            ket_qua.append(p[:i] + [n] + p[i:])
    return ket_qua

n = int(input("Nhập số n: "))
ds = permutation(n)
print(f"Tất cả các hoán vị của [1..{n}] là:")
for p in ds:
    print(p)
