def hoan_vi(lst):
    if len(lst) == 1:
        return [lst]
    result = []
    for i in range(len(lst)):
        x = lst[i]
        sublist = lst[:i] + lst[i+1:]
        for p in hoan_vi(sublist):
            result.append([x] + p)
    return result
n = int(input("Nhập số tự nhiên n: "))
day = list(range(1, n + 1))
cac_hoan_vi = hoan_vi(day)
print(f"Tất cả các hoán vị của dãy [1, 2, ..., {n}]:")
for p in cac_hoan_vi:
    print(p)
