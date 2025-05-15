n = int(input("Nhập số phần tử n: "))
a = []
for i in range(n):
    x = int(input(f"Nhập a[{i}]: "))
    a.append(x)
cặp = []
for i in range(n):
    for j in range(i + 1, n):
        if a[i] + a[j] == a[i] * a[j]:
            cặp.append((i, j))
print("Số cặp chỉ số thỏa mãn:", len(cặp))
print("Các cặp chỉ số:", cặp)