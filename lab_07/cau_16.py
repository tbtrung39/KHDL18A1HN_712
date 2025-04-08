a = list(map(int, input("Nhập dãy số: ").split()))
n = len(a)

for i in range(n):
    for j in range(i+1, n):
        if a[i] + 1 == a[j]:
            print(f"({i}, {j})")
