a = list(map(int, input("Nhập dãy số (cách nhau bởi dấu cách): ").split()))
m = len(a)
count = 0
cap_so = []
for i in range(m):
    for j in range(i+1, m):
        if i + j < m and a[i] + a[j] == a[i + j]:
            count += 1
            cap_so.append((i, j))
print("Tổng số cặp thỏa điều kiện:", count)
print("Các cặp:", cap_so)