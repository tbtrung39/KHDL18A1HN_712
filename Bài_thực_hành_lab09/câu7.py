def find_combinations(n, N, current=[], index=0):
    if index == n:
        if sum(current) == N:
            print(current)
        return
    for i in range(1, N - sum(current) - (n - index - 1) + 1):
        find_combinations(n, N, current + [i], index + 1)

n = int(input("Nhập số lượng phần tử n: "))
N = int(input("Nhập tổng cần đạt N: "))

print(f"Các bộ nghiệm của x1 + x2 + ... + x{n} = {N} là:")
find_combinations(n, N)
