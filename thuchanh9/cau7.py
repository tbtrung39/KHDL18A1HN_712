def solve(n, N, start, curr):
    if len(curr) == n:
        if sum(curr) == N:
            print(curr)
        return
    
    for i in range(start, N + 1):
        solve(n, N, i, curr + [i])

n = int(input("Nhập số n: "))
N = int(input("Nhập số N: "))

solve(n, N, 1, [])
