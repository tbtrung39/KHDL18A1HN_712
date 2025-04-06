a = list(map(int, input("Nhập dãy số, cách nhau bởi dấu cách: ").split()))
n = len(a)
count = 0
pairs = []
for i in range(n):
    for j in range(i+1, n):
        if i + j < n and a[i] + a[j] == a[i + j]:
            count += 1
            pairs.append((i, j))
print("Tổng số cặp thỏa điều kiện:", count)
print("Các cặp:", pairs)
