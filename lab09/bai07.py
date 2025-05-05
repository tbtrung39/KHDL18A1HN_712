def solve(n, N, result, current):
    if n == 1:
        current.append(N)
        result.append(current.copy())
        current.pop()
        return
    for i in range(1, N):
        current.append(i)
        solve(n-1, N-i, result, current)
        current.pop()

n = int(input("Nhập số n: "))
N = int(input("Nhập tổng N: "))
result = []
solve(n, N, result, [])
print("Các bộ nghiệm:")
for r in result:
    print(r)