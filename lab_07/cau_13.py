s = input("Nhập chuỗi: ")
d = {}

for i in range(len(s)):
    for j in range(i+1, len(s)+1):
        sub = s[i:j]
        d[sub] = d.get(sub, 0) + 1

print(d)
