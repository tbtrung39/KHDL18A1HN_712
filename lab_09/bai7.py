def find_partitions(n, k, current=[]):
    if k == 1:
        current.append(n)
        print(current)
        current.pop()
        return
    for i in range(1, n - k + 2):
        current.append(i)
        find_partitions(n - i, k - 1, current)
        current.pop()

N = int(input("Nhập tổng N: "))
n = int(input("Nhập số phần tử n: "))
print(f"Các bộ nghiệm của {N} = x1 + x2 + ... + x{n} là:")
find_partitions(N, n)