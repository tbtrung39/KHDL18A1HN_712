n = int(input())
a = []
for _ in range(n):
    a.append(int(input()))

a[0:0] = [1, 2, 3]
a[5:5] = [1, 2, 3]
a.extend([1, 2, 3])
print(a)

k = int(input())
if 0 <= k < len(a):
    del a[k]
print(a)

b = a[:]
b.sort()
print(b)

c = a[:]
c.sort(reverse=True)
print(c)
