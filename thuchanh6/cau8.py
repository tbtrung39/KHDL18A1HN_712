n = int(input())
a = [0, 1]
for i in range(2, n):
    a.append(a[i-1] + a[i-2])
print(', '.join(str(x) for x in a[:n]))
