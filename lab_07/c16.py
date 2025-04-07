a = [1, 2, 3, 4, 2]
n = len(a)
pairs = []

for i in range(n):
    for j in range(i + 1, n):
        if a[i] + a[j] == 5:
            pairs.append((i, j))

print("Các cặp chỉ số (i, j) sao cho a[i] + a[j] = 5 là:")
print(pairs)
