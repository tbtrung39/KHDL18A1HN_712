s = input("Nhập chuỗi: ")
d = {}

for c in s:
    d[c] = d.get(c, 0) + 1

print("Tần suất xuất hiện ký tự:")
for k, v in d.items():
    print(f"{k}: {v}")
