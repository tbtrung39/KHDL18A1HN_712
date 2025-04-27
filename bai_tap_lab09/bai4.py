import itertools

n = int(input("Nhập n: "))
perm = itertools.permutations(range(1, n+1))

print("Các hoán vị của dãy:")
for p in perm:
    print(p)
