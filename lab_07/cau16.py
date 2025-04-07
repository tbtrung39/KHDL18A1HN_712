a = list(map(int, input("Nhập các số nguyên (cách nhau bởi dấu cách): ").split()))
n = len(a)
pairs = []

for i in range(n):
    for j in range(i, n):
        if a[i] + 1 == a[j]:
            pairs.append((i, j))

print("Các cặp chỉ số (i, j):", pairs)