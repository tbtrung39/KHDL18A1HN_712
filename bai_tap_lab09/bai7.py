def find_solutions(n, total, current=[], start=1):
    if n == 0 and total == 0:
        print(current)
        return
    if n == 0 or total <= 0:
        return
    for i in range(start, total + 1):
        find_solutions(n - 1, total - i, current + [i], i)

n = int(input("Nhập số lượng phần tử n: "))
N = int(input("Nhập tổng cần tìm N: "))

print(f"Các bộ nghiệm x1 + x2 + ... + x{n} = {N} là:")
find_solutions(n, N)
