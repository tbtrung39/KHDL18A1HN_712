a = []
while True:
    x = int(input())
    if x == 0:
        break
    a.append(x)

b = []
for x in a:
    if x > 0:
        b.append(x)
for x in a:
    if x <= 0:
        b.append(x)
print(b)

m = int(input())
a.insert(0, m)
a.append(m)
if len(a) >= 4:
    a.insert(4, m)
else:
    a.append(m)
print(a)
